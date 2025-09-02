import pygame
from settings import *

class LevelCompleteState:
    def __init__(self, asset_loader, game_state_manager, level_number, score):
        self.asset_loader = asset_loader
        self.game_state_manager = game_state_manager
        self.level_number = level_number
        self.score = score
        self.display_time = 0
        self.display_duration = 4000  # 4 seconds for celebration
        self.sound_played = False
        self.celebration_particles = []
        self.celebration_time = 0

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Press Space to continue
                if self.level_number == 1:
                    # Start level 2
                    self.game_state_manager.states[GAME_STATE_PLAYING].level_manager.start_level_2()
                    self.game_state_manager.set_state(GAME_STATE_PLAYING)
                else:
                    # Game completed
                    self.game_state_manager.set_state(GAME_STATE_GAME_OVER, 
                                                    final_score=self.score, 
                                                    final_distance=LEVEL2_DISTANCE,
                                                    victory=True)

    def update(self, dt):
        # Play level complete sound once
        if not self.sound_played:
            sound_manager = self.game_state_manager.sound_manager
            sound_manager.play_level_complete_sound()
            self.sound_played = True
            
        # Update celebration particles
        self.celebration_time += dt
        if self.celebration_time < 2.0:  # Create particles for 2 seconds
            # Create celebration particles
            for _ in range(3):
                particle = {
                    'x': SCREEN_WIDTH // 2 + (pygame.time.get_ticks() % 200 - 100),
                    'y': SCREEN_HEIGHT // 2,
                    'vx': (pygame.time.get_ticks() % 200 - 100) * 0.1,
                    'vy': -200 - (pygame.time.get_ticks() % 100),
                    'color': (255, 215, 0),  # Gold
                    'size': 5 + (pygame.time.get_ticks() % 10),
                    'life': 2.0
                }
                self.celebration_particles.append(particle)
        
        # Update existing particles
        for particle in self.celebration_particles[:]:
            particle['x'] += particle['vx'] * dt
            particle['y'] += particle['vy'] * dt
            particle['vy'] += 500 * dt  # Gravity
            particle['life'] -= dt
            
            if particle['life'] <= 0:
                self.celebration_particles.remove(particle)
            
        self.display_time += dt * 1000  # Convert to milliseconds
        if self.display_time >= self.display_duration:
            # Auto-continue after display duration
            if self.level_number == 1:
                self.game_state_manager.states[GAME_STATE_PLAYING].level_manager.start_level_2()
                self.game_state_manager.set_state(GAME_STATE_PLAYING)
            else:
                self.game_state_manager.set_state(GAME_STATE_GAME_OVER, 
                                                final_score=self.score, 
                                                final_distance=LEVEL2_DISTANCE,
                                                victory=True)

    def draw(self, screen):
        # Draw background
        if self.level_number == 1:
            screen.blit(self.asset_loader.get_image("level1_park_bg"), (0, 0))
        else:
            screen.blit(self.asset_loader.get_image("level2_industrial_bg"), (0, 0))
        
        # Dark overlay
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 150))
        screen.blit(overlay, (0, 0))

        # Draw celebration particles
        for particle in self.celebration_particles:
            alpha = int(255 * (particle['life'] / 2.0))
            color = (*particle['color'][:3], alpha)
            particle_surface = pygame.Surface((particle['size'], particle['size']), pygame.SRCALPHA)
            pygame.draw.circle(particle_surface, color, (particle['size']//2, particle['size']//2), particle['size']//2)
            screen.blit(particle_surface, (particle['x'] - particle['size']//2, particle['y'] - particle['size']//2))

        # Draw level complete message with celebration effect
        font_large = pygame.font.Font(None, 72)
        complete_text = font_large.render(f"LEVEL {self.level_number} COMPLETE!", True, GOLD)
        complete_rect = complete_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100))
        screen.blit(complete_text, complete_rect)

        # Draw score
        font_medium = pygame.font.Font(None, 48)
        score_text = font_medium.render(f"Score: {self.score}", True, WHITE)
        score_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
        screen.blit(score_text, score_rect)

        # Draw instruction
        font_small = pygame.font.Font(None, 36)
        if self.level_number == 1:
            instruction_text = font_small.render("Press SPACE to continue to Level 2", True, WHITE)
        else:
            instruction_text = font_small.render("Press SPACE to finish game", True, WHITE)
        instruction_rect = instruction_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
        screen.blit(instruction_text, instruction_rect)
