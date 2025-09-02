import pygame
import sys
from settings import *

class GameOverState:
    def __init__(self, asset_loader, game_state_manager, final_score, final_distance, victory=False):
        self.asset_loader = asset_loader
        self.game_state_manager = game_state_manager
        self.final_score = final_score
        self.final_distance = final_distance
        self.victory = victory
        self.sound_played = False
        self.celebration_particles = []
        self.celebration_time = 0

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:  # Restart game
                self.game_state_manager.set_state(GAME_STATE_PLAYING)
                # Reset game state in PlayingState
                self.game_state_manager.states[GAME_STATE_PLAYING].reset_game()
            if event.key == pygame.K_q:  # Quit game
                pygame.quit()
                sys.exit()

    def update(self, dt):
        # Play victory sound once if player won
        if self.victory and not self.sound_played:
            sound_manager = self.game_state_manager.sound_manager
            sound_manager.play_victory_sound()
            self.sound_played = True

        # Update celebration particles for victory
        if self.victory:
            self.celebration_time += dt
            if self.celebration_time < 3.0:  # Create particles for 3 seconds
                # Create celebration particles
                for _ in range(5):
                    particle = {
                        'x': SCREEN_WIDTH // 2 + (pygame.time.get_ticks() % 300 - 150),
                        'y': SCREEN_HEIGHT // 2,
                        'vx': (pygame.time.get_ticks() % 300 - 150) * 0.15,
                        'vy': -300 - (pygame.time.get_ticks() % 150),
                        'color': (255, 215, 0),  # Gold
                        'size': 8 + (pygame.time.get_ticks() % 15),
                        'life': 3.0
                    }
                    self.celebration_particles.append(particle)
            
            # Update existing particles
            for particle in self.celebration_particles[:]:
                particle['x'] += particle['vx'] * dt
                particle['y'] += particle['vy'] * dt
                particle['vy'] += 400 * dt  # Gravity
                particle['life'] -= dt
                
                if particle['life'] <= 0:
                    self.celebration_particles.remove(particle)

    def draw(self, screen):
        screen.fill(BLACK)
        
        if self.victory:
            # Victory screen with celebration
            # Draw celebration particles
            for particle in self.celebration_particles:
                alpha = int(255 * (particle['life'] / 3.0))
                color = (*particle['color'][:3], alpha)
                particle_surface = pygame.Surface((particle['size'], particle['size']), pygame.SRCALPHA)
                pygame.draw.circle(particle_surface, color, (particle['size']//2, particle['size']//2), particle['size']//2)
                screen.blit(particle_surface, (particle['x'] - particle['size']//2, particle['y'] - particle['size']//2))

            font_large = pygame.font.Font(None, 72)
            victory_text = font_large.render("VICTORY!", True, GOLD)
            victory_rect = victory_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 150))
            screen.blit(victory_text, victory_rect)
            
            font_medium = pygame.font.Font(None, 48)
            congrats_text = font_medium.render("You completed both levels!", True, WHITE)
            congrats_rect = congrats_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100))
            screen.blit(congrats_text, congrats_rect)
        else:
            # Game over screen
            font_large = pygame.font.Font(None, 72)
            game_over_text = font_large.render("GAME OVER", True, RED)
            game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 150))
            screen.blit(game_over_text, game_over_rect)

        # Draw final stats
        font_medium = pygame.font.Font(None, 36)
        score_text = font_medium.render(f"Final Score: {self.final_score}", True, WHITE)
        score_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
        screen.blit(score_text, score_rect)

        distance_text = font_medium.render(f"Distance: {self.final_distance:.1f}m", True, WHITE)
        distance_rect = distance_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(distance_text, distance_rect)

        # Draw progress to goal
        progress_text = font_medium.render(f"Progress: {(self.final_distance / LEVEL2_DISTANCE) * 100:.1f}%", True, WHITE)
        progress_rect = progress_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
        screen.blit(progress_text, progress_rect)

        # Draw restart/quit instructions
        font_small = pygame.font.Font(None, 28)
        restart_text = font_small.render("Press 'R' to Restart or 'Q' to Quit", True, WHITE)
        restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 120))
        screen.blit(restart_text, restart_rect)


