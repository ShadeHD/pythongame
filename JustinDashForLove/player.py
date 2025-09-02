import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, asset_loader):
        super().__init__()
        self.asset_loader = asset_loader
        self.image = self.asset_loader.get_image("justin")
        self.original_image = self.image.copy()
        
        # Scale image to proper size and remove background
        self.image = pygame.transform.scale(self.image, (PLAYER_SIZE, PLAYER_SIZE))
        self.original_image = pygame.transform.scale(self.original_image, (PLAYER_SIZE, PLAYER_SIZE))
        
        # Remove background from character image
        self.image = self.remove_background(self.image)
        self.original_image = self.remove_background(self.original_image)
        
        self.rect = self.image.get_rect()
        self.rect.center = (LANE_POSITIONS[2], SCREEN_HEIGHT - 200)  # Start in center lane
        
        # Movement - ACTUAL Subway Surfers style
        self.current_lane_index = 2  # 0-4: 5 lanes
        self.target_x = LANE_POSITIONS[2]
        self.y_velocity = 0
        self.is_jumping = False
        self.is_sliding = False
        self.slide_start_y = 0
        
        # Forward movement - player moves forward at constant speed
        self.forward_speed = PLAYER_FORWARD_SPEED
        self.distance_traveled = 0
        
        # Power-up effects
        self.has_shield = False
        self.shield_end_time = 0
        self.has_magnet = False
        self.magnet_end_time = 0
        self.has_speed_boost = False
        self.speed_boost_end_time = 0
        self.coins_collected = 0
        
        # Love power-up effects
        self.has_love_hug = False
        self.love_hug_end_time = 0
        self.has_couple_power = False
        self.couple_power_end_time = 0
        self.has_love_call = False
        self.love_call_end_time = 0
        self.is_invincible = False
        self.invincibility_end_time = 0
        
        # Game stats
        self.score = 0
        
        # Sound settings - DISABLED movement sounds
        self.sound_enabled = False  # Disabled to remove annoying beeping

    def remove_background(self, image):
        """Remove background from character image"""
        # Create a surface with alpha channel
        surface = pygame.Surface(image.get_size(), pygame.SRCALPHA)
        
        # Get the color of the top-left pixel (assumed to be background)
        bg_color = image.get_at((0, 0))
        
        # Copy pixels, but make background transparent
        for x in range(image.get_width()):
            for y in range(image.get_height()):
                pixel = image.get_at((x, y))
                # If pixel is close to background color, make it transparent
                if abs(pixel[0] - bg_color[0]) < 30 and abs(pixel[1] - bg_color[1]) < 30 and abs(pixel[2] - bg_color[2]) < 30:
                    surface.set_at((x, y), (0, 0, 0, 0))  # Transparent
                else:
                    surface.set_at((x, y), pixel)
        
        return surface

    def update(self, dt):
        current_time = pygame.time.get_ticks()

        # Check power-up durations
        if self.has_shield and current_time > self.shield_end_time:
            self.has_shield = False
        if self.has_magnet and current_time > self.magnet_end_time:
            self.has_magnet = False
        if self.has_speed_boost and current_time > self.speed_boost_end_time:
            self.has_speed_boost = False
        if self.has_love_hug and current_time > self.love_hug_end_time:
            self.has_love_hug = False
        if self.has_couple_power and current_time > self.couple_power_end_time:
            self.has_couple_power = False
        if self.has_love_call and current_time > self.love_call_end_time:
            self.has_love_call = False
        if self.is_invincible and current_time > self.invincibility_end_time:
            self.is_invincible = False

        # Apply gravity if jumping
        if self.is_jumping:
            self.y_velocity += PLAYER_GRAVITY * dt
            self.rect.y += self.y_velocity * dt
            
            # Check if landed
            if self.rect.bottom >= SCREEN_HEIGHT - 200:
                self.rect.bottom = SCREEN_HEIGHT - 200
                self.is_jumping = False
                self.y_velocity = 0

        # Smooth lane change - EVEN SMOOTHER like Subway Surfers
        if abs(self.rect.centerx - self.target_x) > 1:
            if self.rect.centerx < self.target_x:
                self.rect.centerx += PLAYER_LANE_CHANGE_SPEED * dt
            else:
                self.rect.centerx -= PLAYER_LANE_CHANGE_SPEED * dt
        else:
            self.rect.centerx = self.target_x

        # Update distance traveled (player moves forward)
        self.distance_traveled += self.forward_speed * dt
        self.score += int(10 * dt)

    def draw(self, screen):
        # Draw the player
        screen.blit(self.image, self.rect)
        
        # Draw power-up indicators
        if self.has_shield:
            pygame.draw.circle(screen, BLUE, self.rect.center, self.rect.width // 2 + 15, 4)
        if self.has_magnet:
            pygame.draw.circle(screen, GREEN, self.rect.center, self.rect.width // 2 + 20, 3)
        if self.has_speed_boost:
            # Draw speed lines behind the player
            for i in range(5):
                start_pos = (self.rect.left - 30 - i * 8, self.rect.centery + i * 3)
                end_pos = (self.rect.left - 10 - i * 8, self.rect.centery + i * 3)
                pygame.draw.line(screen, RED, start_pos, end_pos, 3)
        if self.is_invincible:
            # Draw invincibility sparkles
            pygame.draw.circle(screen, GOLD, self.rect.center, self.rect.width // 2 + 25, 2)
        if self.has_love_hug:
            # Draw love hug effect (pink circle)
            pygame.draw.circle(screen, (255, 100, 150), self.rect.center, self.rect.width // 2 + 30, 3)
        if self.has_couple_power:
            # Draw couple power effect (purple circle)
            pygame.draw.circle(screen, (150, 100, 255), self.rect.center, self.rect.width // 2 + 35, 3)
        if self.has_love_call:
            # Draw love call effect (light blue circle)
            pygame.draw.circle(screen, (100, 200, 255), self.rect.center, self.rect.width // 2 + 40, 3)

    def jump(self):
        if not self.is_jumping and not self.is_sliding:
            self.is_jumping = True
            self.y_velocity = -PLAYER_JUMP_HEIGHT
            # NO SOUND - removed annoying beeping

    def slide(self):
        if not self.is_jumping and not self.is_sliding:
            self.is_sliding = True
            self.slide_start_y = self.rect.y
            
            # Scale down the image for sliding
            slide_height = int(PLAYER_SIZE * 0.6)
            self.image = pygame.transform.scale(self.original_image, (PLAYER_SIZE, slide_height))
            self.rect = self.image.get_rect(center=self.rect.center)
            self.rect.y = self.slide_start_y + (PLAYER_SIZE - slide_height)
            
            # NO SOUND - removed annoying beeping

    def stop_slide(self):
        if self.is_sliding:
            self.is_sliding = False
            self.image = self.original_image
            self.rect = self.image.get_rect(center=self.rect.center)
            self.rect.y = self.slide_start_y

    def move_left(self):
        if self.current_lane_index > 0:
            self.current_lane_index -= 1
            self.target_x = LANE_POSITIONS[self.current_lane_index]

    def move_right(self):
        if self.current_lane_index < len(LANE_POSITIONS) - 1:
            self.current_lane_index += 1
            self.target_x = LANE_POSITIONS[self.current_lane_index]

    def check_collision(self, obstacle_rect):
        if self.has_shield or self.is_invincible:
            return False  # Shield or invincibility protects from collisions
        return self.rect.colliderect(obstacle_rect)

    def collect_coin(self):
        self.coins_collected += 1
        self.score += 50

    def activate_shield(self, duration):
        self.has_shield = True
        self.shield_end_time = pygame.time.get_ticks() + duration

    def activate_magnet(self, duration):
        self.has_magnet = True
        self.magnet_end_time = pygame.time.get_ticks() + duration

    def activate_speed_boost(self, duration):
        self.has_speed_boost = True
        self.speed_boost_end_time = pygame.time.get_ticks() + duration

    # Love power-up methods
    def collect_kiss(self):
        """Kiss power-up: Gives points and temporary invincibility"""
        self.coins_collected += 1
        self.score += 100
        self.is_invincible = True
        self.invincibility_end_time = pygame.time.get_ticks() + 3000  # 3 seconds invincibility

    def activate_love_hug(self, duration):
        """Love hug power-up: Attracts nearby power-ups"""
        self.has_love_hug = True
        self.love_hug_end_time = pygame.time.get_ticks() + duration

    def activate_couple_power(self, duration):
        """Couple power-up: Double points for a short time"""
        self.has_couple_power = True
        self.couple_power_end_time = pygame.time.get_ticks() + duration

    def activate_love_call(self, duration):
        """Love call power-up: Slows down obstacles temporarily"""
        self.has_love_call = True
        self.love_call_end_time = pygame.time.get_ticks() + duration

    def reset(self):
        self.rect.center = (LANE_POSITIONS[2], SCREEN_HEIGHT - 200)
        self.current_lane_index = 2
        self.target_x = LANE_POSITIONS[2]
        self.y_velocity = 0
        self.is_jumping = False
        self.is_sliding = False
        self.image = self.original_image
        self.distance_traveled = 0
        self.score = 0
        self.coins_collected = 0
        self.has_shield = False
        self.has_magnet = False
        self.has_speed_boost = False
        self.has_love_hug = False
        self.has_couple_power = False
        self.has_love_call = False
        self.is_invincible = False


