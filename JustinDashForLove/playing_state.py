import pygame
from settings import *
from player import Player
from level_manager import LevelManager
from sound_manager import SoundManager
from particle_manager import ParticleManager

class PlayingState:
    def __init__(self, asset_loader, game_state_manager):
        self.asset_loader = asset_loader
        self.game_state_manager = game_state_manager
        self.player = Player(asset_loader)
        self.level_manager = LevelManager(asset_loader)
        self.sound_manager = SoundManager(asset_loader)
        self.particle_manager = ParticleManager()
        self.game_started = False

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                self.player.jump()
            if event.key == pygame.K_DOWN:
                self.player.slide()
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                self.player.move_left()
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                self.player.move_right()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                self.player.stop_slide()

    def update(self, dt):
        if not self.game_started:
            self.game_started = True
            self.sound_manager.play_music("level1_music")

        self.player.update(dt)
        self.level_manager.update(dt)
        self.particle_manager.update(dt)

        # Move obstacles and powerups DOWN (player moves forward)
        for obstacle in self.level_manager.obstacles:
            obstacle.rect.y += self.player.forward_speed * dt
            
        for powerup in self.level_manager.powerups:
            powerup.rect.y += self.player.forward_speed * dt

        # Check for collisions with obstacles
        for obstacle in self.level_manager.obstacles:
            if self.player.check_collision(obstacle.rect):
                self.sound_manager.play_sfx("collision_sfx")  # CRASH SOUND
                self.particle_manager.create_explosion(self.player.rect.center, RED)
                self.game_state_manager.set_state(GAME_STATE_GAME_OVER, 
                                                final_score=self.player.score, 
                                                final_distance=self.level_manager.distance)

        # Check for collisions with powerups
        for powerup in self.level_manager.powerups:
            if self.player.check_collision(powerup.rect):
                self.sound_manager.play_sfx("coin_sfx")  # KISS SOUND
                powerup.apply_effect(self.player)
                # Create kiss emoji particles instead of gold
                self.create_kiss_particles(powerup.rect.center)
                powerup.kill()

        # Check for level completion
        if self.level_manager.check_level_completion() and not self.level_manager.level_completed:
            self.level_manager.level_completed = True
            # Play level complete sound
            self.sound_manager.play_level_complete_sound()
            # Show level complete screen
            self.game_state_manager.set_state(GAME_STATE_LEVEL_COMPLETE, 
                                            level_number=self.level_manager.current_level,
                                            score=self.player.score)

        # Check for game completion (both levels done)
        if self.level_manager.check_game_completion():
            # Play victory sound
            self.sound_manager.play_victory_sound()
            # Player won - completed both levels
            self.game_state_manager.set_state(GAME_STATE_GAME_OVER, 
                                            final_score=self.player.score, 
                                            final_distance=self.level_manager.distance,
                                            victory=True)

        # Check for game timeout
        if self.level_manager.check_game_timeout():
            # Time's up
            self.game_state_manager.set_state(GAME_STATE_GAME_OVER, 
                                            final_score=self.player.score, 
                                            final_distance=self.level_manager.distance)

    def create_kiss_particles(self, position):
        """Create kiss emoji particles"""
        for i in range(5):
            particle = {
                'x': position[0],
                'y': position[1],
                'vx': (i - 2) * 50,
                'vy': -100 - i * 20,
                'color': (255, 255, 0),  # Yellow for kiss emoji
                'size': 8 + i * 2,
                'life': 1.5,
                'type': 'kiss'
            }
            self.particle_manager.add_custom_particle(particle)

    def draw(self, screen):
        # Draw background based on level
        if self.level_manager.current_level == 1:
            screen.blit(self.asset_loader.get_image("level1_park_bg"), (0, 0))
        else:
            screen.blit(self.asset_loader.get_image("level2_industrial_bg"), (0, 0))

        self.player.draw(screen)
        self.level_manager.draw(screen)
        self.particle_manager.draw(screen)

        # Draw UI
        self.draw_ui(screen)

    def draw_ui(self, screen):
        font_large = pygame.font.Font(None, 48)
        font_medium = pygame.font.Font(None, 36)
        font_small = pygame.font.Font(None, 24)

        # Draw level indicator
        level_text = font_medium.render(f"Level {self.level_manager.current_level}", True, WHITE)
        screen.blit(level_text, (10, 10))

        # Draw score
        score_text = font_medium.render(f"Score: {self.player.score}", True, WHITE)
        screen.blit(score_text, (10, 40))

        # Draw distance progress
        target_distance = self.level_manager.get_target_distance()
        distance_text = font_medium.render(f"Distance: {self.level_manager.distance:.1f}m / {target_distance}m", True, WHITE)
        screen.blit(distance_text, (10, 70))

        # Draw progress bar
        progress_width = 300
        progress_height = 20
        progress_x = SCREEN_WIDTH // 2 - progress_width // 2
        progress_y = 20
        
        # Background bar
        pygame.draw.rect(screen, (100, 100, 100), (progress_x, progress_y, progress_width, progress_height))
        
        # Progress fill
        progress_fill = (self.level_manager.distance / target_distance) * progress_width
        pygame.draw.rect(screen, GREEN, (progress_x, progress_y, progress_fill, progress_height))
        
        # Progress border
        pygame.draw.rect(screen, WHITE, (progress_x, progress_y, progress_width, progress_height), 2)

        # Draw remaining time
        remaining_time = self.level_manager.get_remaining_time()
        time_text = font_medium.render(f"Time: {remaining_time:.1f}s", True, WHITE)
        screen.blit(time_text, (SCREEN_WIDTH - 200, 10))

        # Draw controls hint
        controls_text = font_small.render("Arrow Keys: Move | Space: Jump | Down: Slide", True, WHITE)
        screen.blit(controls_text, (10, SCREEN_HEIGHT - 30))

        # Draw power-up indicators
        y_offset = 100
        if self.player.has_shield:
            shield_text = font_small.render("SHIELD ACTIVE", True, BLUE)
            screen.blit(shield_text, (10, y_offset))
            y_offset += 25
        if self.player.has_magnet:
            magnet_text = font_small.render("MAGNET ACTIVE", True, GREEN)
            screen.blit(magnet_text, (10, y_offset))
            y_offset += 25
        if self.player.has_speed_boost:
            speed_text = font_small.render("SPEED BOOST ACTIVE", True, RED)
            screen.blit(speed_text, (10, y_offset))

    def reset_game(self):
        self.player.reset()
        self.level_manager.reset()
        self.game_started = False


