import pygame
import sys
from settings import *
from menu_state import MenuState
from playing_state import PlayingState
from game_over_state import GameOverState
from intro_state import IntroState
from level_complete_state import LevelCompleteState

class GameStateManager:
    def __init__(self, initial_state, asset_loader, sound_manager):
        self.asset_loader = asset_loader
        self.sound_manager = sound_manager
        self.states = {
            GAME_STATE_MENU: MenuState(self.asset_loader, self),
            GAME_STATE_PLAYING: PlayingState(self.asset_loader, self),
            GAME_STATE_INTRO: IntroState(self.asset_loader, self),
            # GAME_STATE_GAME_OVER and GAME_STATE_LEVEL_COMPLETE will be initialized dynamically
        }
        self.current_state = self.states[initial_state]

    def get_state(self):
        return self.current_state

    def set_state(self, new_state_id, **kwargs):
        if new_state_id == GAME_STATE_GAME_OVER:
            victory = kwargs.get("victory", False)
            self.current_state = GameOverState(self.asset_loader, self, 
                                             kwargs["final_score"], 
                                             kwargs["final_distance"], 
                                             victory)
        elif new_state_id == GAME_STATE_LEVEL_COMPLETE:
            self.current_state = LevelCompleteState(self.asset_loader, self,
                                                  kwargs["level_number"],
                                                  kwargs["score"])
        else:
            self.current_state = self.states[new_state_id]

    def handle_input(self, event):
        self.current_state.handle_input(event)

    def update(self, dt):
        self.current_state.update(dt)

    def draw(self, screen):
        self.current_state.draw(screen)


