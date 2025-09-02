import pygame
from settings import *

class MenuState:
    def __init__(self, asset_loader, game_state_manager):
        self.asset_loader = asset_loader
        self.game_state_manager = game_state_manager

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:  # Press Enter to start game
                self.game_state_manager.set_state(GAME_STATE_PLAYING)

    def update(self, dt):
        pass

    def draw(self, screen):
        # Draw background
        screen.blit(self.asset_loader.get_image("level1_park_bg"), (0, 0))
        
        # Dark overlay
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 150))
        screen.blit(overlay, (0, 0))

        # Draw title
        font_large = pygame.font.Font(None, 72)
        title_text = font_large.render("Justin's Dash for Love", True, GOLD)
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100))
        screen.blit(title_text, title_rect)

        # Draw subtitle
        font_medium = pygame.font.Font(None, 36)
        subtitle_text = font_medium.render("Subway Surfers Style Runner", True, WHITE)
        subtitle_rect = subtitle_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
        screen.blit(subtitle_text, subtitle_rect)

        # Draw instructions
        font_small = pygame.font.Font(None, 28)
        start_text = font_small.render("Press ENTER to Start", True, WHITE)
        start_rect = start_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
        screen.blit(start_text, start_rect)

        # Draw game info
        info_text = font_small.render("Level 1: 1 minute | Level 2: 2 minutes", True, WHITE)
        info_rect = info_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100))
        screen.blit(info_text, info_rect)


