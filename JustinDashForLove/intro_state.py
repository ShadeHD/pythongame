import pygame
import sys
from settings import *

class IntroState:
    def __init__(self, asset_loader, game_state_manager):
        self.asset_loader = asset_loader
        self.game_state_manager = game_state_manager
        self.background = self.asset_loader.get_image("level1_park_bg")
        self.font_large = pygame.font.Font(None, 48)
        self.font_medium = pygame.font.Font(None, 36)
        self.font_small = pygame.font.Font(None, 24)
        self.story_text = [
            "Justin's Dash for Love",
            "Run 100 meters in 2 minutes!",
            "Avoid obstacles and collect power-ups",
            "Use Arrow Keys to move, Space to jump, Down to slide",
            "Press SPACE to start your journey!"
        ]
        self.current_line = 0
        self.line_display_time = 0
        self.line_duration = 2000  # milliseconds per line

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if self.current_line < len(self.story_text) - 1:
                    self.current_line += 1
                    self.line_display_time = pygame.time.get_ticks()
                else:
                    self.game_state_manager.set_state(GAME_STATE_PLAYING)

    def update(self, dt):
        current_time = pygame.time.get_ticks()
        if self.current_line < len(self.story_text) - 1 and current_time - self.line_display_time > self.line_duration:
            self.current_line += 1
            self.line_display_time = current_time

    def draw(self, screen):
        screen.blit(self.background, (0, 0))
        
        # Dark overlay for text readability
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 150))  # Black with 150 alpha
        screen.blit(overlay, (0, 0))

        # Draw title
        title_text = self.font_large.render("Justin's Dash for Love", True, GOLD)
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 150))
        screen.blit(title_text, title_rect)

        # Draw current story text
        text_surface = self.font_medium.render(self.story_text[self.current_line], True, WHITE)
        text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(text_surface, text_rect)

        # Draw controls
        controls_text = self.font_small.render("Arrow Keys: Move | Space: Jump | Down: Slide", True, WHITE)
        controls_rect = controls_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100))
        screen.blit(controls_text, controls_rect)

        # Draw instruction to continue
        instruction_text = self.font_small.render("Press SPACE to continue...", True, WHITE)
        instruction_rect = instruction_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50))
        screen.blit(instruction_text, instruction_rect)


