import pygame
from settings import *

class PowerUp(pygame.sprite.Sprite):
    def __init__(self, asset_loader, x, y, powerup_type, duration):
        super().__init__()
        self.rect = pygame.Rect(x, y, POWERUP_SIZE, POWERUP_SIZE)
        self.rect.x = x
        self.rect.y = y
        self.powerup_type = powerup_type
        self.duration = duration
        self.original_y = y  # Store original Y position
        
        # Use drawn versions for love power-ups (until images are added)
        if powerup_type in ["kiss", "love_hug", "couple", "love_call"]:
            self.image = self.create_fallback_powerup()
        else:
            # Fallback for other power-ups
            self.image = pygame.Surface((POWERUP_SIZE, POWERUP_SIZE), pygame.SRCALPHA)
            pygame.draw.circle(self.image, (255, 255, 0), (POWERUP_SIZE//2, POWERUP_SIZE//2), POWERUP_SIZE//2)

    def load_love_powerup_image(self, asset_loader):
        """Load actual love power-up images"""
        try:
            image = asset_loader.get_image(self.powerup_type)
            
            if image:
                # Scale the image to the power-up size
                scaled_image = pygame.transform.scale(image, (POWERUP_SIZE, POWERUP_SIZE))
                return scaled_image
            else:
                # Fallback if image not found
                return self.create_fallback_powerup()
        except:
            # Fallback if any error occurs
            return self.create_fallback_powerup()
    
    def create_fallback_powerup(self):
        """Create a fallback power-up if image loading fails"""
        surface = pygame.Surface((POWERUP_SIZE, POWERUP_SIZE), pygame.SRCALPHA)
        
        if self.powerup_type == "kiss":
            self.draw_kiss_powerup(surface)
        elif self.powerup_type == "love_hug":
            self.draw_love_hug_powerup(surface)
        elif self.powerup_type == "couple":
            self.draw_couple_powerup(surface)
        elif self.powerup_type == "love_call":
            self.draw_love_call_powerup(surface)
        else:
            pygame.draw.circle(surface, (255, 255, 0), (POWERUP_SIZE//2, POWERUP_SIZE//2), POWERUP_SIZE//2)
        
        return surface
    
    def draw_kiss_powerup(self, surface):
        """Draw red lip print power-up - BIGGER and more noticeable"""
        # Glowing background
        glow_color = (255, 200, 200)
        pygame.draw.circle(surface, glow_color, (POWERUP_SIZE//2, POWERUP_SIZE//2), POWERUP_SIZE//2)
        
        # Main lip shape
        lip_color = (255, 50, 50)
        pygame.draw.ellipse(surface, lip_color, (POWERUP_SIZE//6, POWERUP_SIZE//4, 2*POWERUP_SIZE//3, POWERUP_SIZE//2))
        
        # Lip outline
        pygame.draw.ellipse(surface, (200, 30, 30), (POWERUP_SIZE//6, POWERUP_SIZE//4, 2*POWERUP_SIZE//3, POWERUP_SIZE//2), 3)
        
        # Cupid's bow detail
        pygame.draw.arc(surface, (200, 30, 30), (POWERUP_SIZE//4, POWERUP_SIZE//4, POWERUP_SIZE//2, POWERUP_SIZE//3), 0, 3.14, 3)
        
        # Sparkle effect
        sparkle_color = (255, 255, 255)
        pygame.draw.circle(surface, sparkle_color, (POWERUP_SIZE//4, POWERUP_SIZE//4), 3)
        pygame.draw.circle(surface, sparkle_color, (3*POWERUP_SIZE//4, POWERUP_SIZE//4), 3)
    
    def draw_love_hug_powerup(self, surface):
        """Draw heart with arms power-up - BIGGER and more noticeable"""
        # Glowing background
        glow_color = (255, 200, 200)
        pygame.draw.circle(surface, glow_color, (POWERUP_SIZE//2, POWERUP_SIZE//2), POWERUP_SIZE//2)
        
        # Main heart (bigger)
        heart_color = (255, 50, 50)
        pygame.draw.circle(surface, heart_color, (POWERUP_SIZE//3, POWERUP_SIZE//2), POWERUP_SIZE//3)
        pygame.draw.circle(surface, heart_color, (2*POWERUP_SIZE//3, POWERUP_SIZE//2), POWERUP_SIZE//3)
        pygame.draw.polygon(surface, heart_color, [(POWERUP_SIZE//2, POWERUP_SIZE//2 + POWERUP_SIZE//3), 
                                                  (POWERUP_SIZE//4, POWERUP_SIZE//2), 
                                                  (3*POWERUP_SIZE//4, POWERUP_SIZE//2)])
        
        # White arms (bigger)
        arm_color = (255, 255, 255)
        pygame.draw.rect(surface, arm_color, (POWERUP_SIZE//8, POWERUP_SIZE//2, POWERUP_SIZE//4, POWERUP_SIZE//3))
        pygame.draw.rect(surface, arm_color, (5*POWERUP_SIZE//8, POWERUP_SIZE//2, POWERUP_SIZE//4, POWERUP_SIZE//3))
        
        # Hands (bigger)
        pygame.draw.circle(surface, arm_color, (POWERUP_SIZE//6, 3*POWERUP_SIZE//4), POWERUP_SIZE//6)
        pygame.draw.circle(surface, arm_color, (5*POWERUP_SIZE//6, 3*POWERUP_SIZE//4), POWERUP_SIZE//6)
        
        # Sparkle effect
        sparkle_color = (255, 255, 255)
        pygame.draw.circle(surface, sparkle_color, (POWERUP_SIZE//4, POWERUP_SIZE//4), 4)
        pygame.draw.circle(surface, sparkle_color, (3*POWERUP_SIZE//4, POWERUP_SIZE//4), 4)
    
    def draw_couple_powerup(self, surface):
        """Draw two figures in heart power-up - BIGGER and more noticeable"""
        # Glowing background
        glow_color = (255, 200, 200)
        pygame.draw.circle(surface, glow_color, (POWERUP_SIZE//2, POWERUP_SIZE//2), POWERUP_SIZE//2)
        
        # Heart outline (bigger)
        heart_outline = (255, 100, 150)
        pygame.draw.circle(surface, heart_outline, (POWERUP_SIZE//3, POWERUP_SIZE//2), POWERUP_SIZE//2, 4)
        pygame.draw.circle(surface, heart_outline, (2*POWERUP_SIZE//3, POWERUP_SIZE//2), POWERUP_SIZE//2, 4)
        pygame.draw.polygon(surface, heart_outline, [(POWERUP_SIZE//2, POWERUP_SIZE//2 + POWERUP_SIZE//2), 
                                                    (POWERUP_SIZE//8, POWERUP_SIZE//2), 
                                                    (7*POWERUP_SIZE//8, POWERUP_SIZE//2)], 4)
        
        # Blue figure (left) - bigger
        blue_figure = (100, 150, 255)
        pygame.draw.circle(surface, blue_figure, (POWERUP_SIZE//3, POWERUP_SIZE//2), POWERUP_SIZE//4)
        pygame.draw.rect(surface, blue_figure, (POWERUP_SIZE//6, POWERUP_SIZE//2, POWERUP_SIZE//4, POWERUP_SIZE//3))
        
        # Pink figure (right) - bigger
        pink_figure = (255, 150, 200)
        pygame.draw.circle(surface, pink_figure, (2*POWERUP_SIZE//3, POWERUP_SIZE//2), POWERUP_SIZE//4)
        pygame.draw.rect(surface, pink_figure, (7*POWERUP_SIZE//12, POWERUP_SIZE//2, POWERUP_SIZE//4, POWERUP_SIZE//3))
        
        # Small hearts (bigger)
        small_heart = (255, 100, 150)
        pygame.draw.circle(surface, small_heart, (POWERUP_SIZE//2, POWERUP_SIZE//4), 5)
        pygame.draw.circle(surface, small_heart, (POWERUP_SIZE//4, POWERUP_SIZE//4), 4)
        pygame.draw.circle(surface, small_heart, (3*POWERUP_SIZE//4, POWERUP_SIZE//4), 4)
        
        # Sparkle effect
        sparkle_color = (255, 255, 255)
        pygame.draw.circle(surface, sparkle_color, (POWERUP_SIZE//4, POWERUP_SIZE//6), 3)
        pygame.draw.circle(surface, sparkle_color, (3*POWERUP_SIZE//4, POWERUP_SIZE//6), 3)
    
    def draw_love_call_powerup(self, surface):
        """Draw telephone with hearts power-up - BIGGER and more noticeable"""
        # Glowing background
        glow_color = (255, 200, 200)
        pygame.draw.circle(surface, glow_color, (POWERUP_SIZE//2, POWERUP_SIZE//2), POWERUP_SIZE//2)
        
        # Telephone receiver (bigger)
        phone_color = (255, 50, 50)
        pygame.draw.rect(surface, phone_color, (POWERUP_SIZE//6, POWERUP_SIZE//3, 2*POWERUP_SIZE//3, POWERUP_SIZE//4))
        pygame.draw.circle(surface, phone_color, (POWERUP_SIZE//6, POWERUP_SIZE//3), POWERUP_SIZE//6)
        pygame.draw.circle(surface, phone_color, (5*POWERUP_SIZE//6, POWERUP_SIZE//3), POWERUP_SIZE//6)
        
        # Speech bubble (bigger)
        bubble_color = (200, 200, 200)
        pygame.draw.ellipse(surface, bubble_color, (POWERUP_SIZE//2, POWERUP_SIZE//8, POWERUP_SIZE//2, POWERUP_SIZE//3))
        
        # Hearts in bubble (bigger)
        heart1 = (255, 50, 50)
        heart2 = (255, 100, 150)
        pygame.draw.circle(surface, heart1, (2*POWERUP_SIZE//3, POWERUP_SIZE//3), 6)
        pygame.draw.circle(surface, heart2, (2*POWERUP_SIZE//3 + 10, POWERUP_SIZE//3), 5)
        
        # Sparkle effect
        sparkle_color = (255, 255, 255)
        pygame.draw.circle(surface, sparkle_color, (POWERUP_SIZE//4, POWERUP_SIZE//4), 4)
        pygame.draw.circle(surface, sparkle_color, (3*POWERUP_SIZE//4, POWERUP_SIZE//4), 4)

    def update(self, dt):
        # Powerups are STATIC - they don't move
        # The player moves forward past them
        pass

    def apply_effect(self, player):
        if self.powerup_type == "kiss":
            player.collect_kiss()  # Gives points and temporary invincibility
        elif self.powerup_type == "love_hug":
            player.activate_love_hug(self.duration)  # Attracts nearby power-ups
        elif self.powerup_type == "couple":
            player.activate_couple_power(self.duration)  # Double points for a short time
        elif self.powerup_type == "love_call":
            player.activate_love_call(self.duration)  # Slows down obstacles temporarily
        elif self.powerup_type == "shield":
            player.activate_shield(self.duration)
        elif self.powerup_type == "magnet":
            player.activate_magnet(self.duration)
        elif self.powerup_type == "speed_boost":
            player.activate_speed_boost(self.duration)

    def draw(self, screen):
        screen.blit(self.image, self.rect)


