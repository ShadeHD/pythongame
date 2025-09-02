import pygame
from settings import *

class MonsterObstacle(pygame.sprite.Sprite):
    def __init__(self, monster_type, x, y):
        super().__init__()
        self.monster_type = monster_type
        self.rect = pygame.Rect(x, y, OBSTACLE_SIZE, OBSTACLE_SIZE)
        self.original_y = y
        
        # Create colored monster placeholders
        self.image = self.create_monster_placeholder()
        
    def create_monster_placeholder(self):
        """Create detailed monster designs based on the new monster images"""
        surface = pygame.Surface((OBSTACLE_SIZE, OBSTACLE_SIZE), pygame.SRCALPHA)
        
        if self.monster_type == "monster1":
            # Demon monster - Dark with wings, horns, and staff
            self.draw_demon_monster(surface)
        elif self.monster_type == "monster2":
            # Rock golem - Stone-like with sharp features
            self.draw_rock_golem(surface)
        else:  # monster3
            # Werewolf - Muscular wolf-like creature
            self.draw_werewolf(surface)
            
        return surface
    
    def draw_demon_monster(self, surface):
        """Draw the demon monster with wings, horns, and staff"""
        # Main body (dark brown/black)
        body_color = (40, 20, 10)
        pygame.draw.ellipse(surface, body_color, (OBSTACLE_SIZE//4, OBSTACLE_SIZE//3, OBSTACLE_SIZE//2, 2*OBSTACLE_SIZE//3))
        
        # Head with helmet
        head_color = (30, 15, 5)
        pygame.draw.circle(surface, head_color, (OBSTACLE_SIZE//2, OBSTACLE_SIZE//3), OBSTACLE_SIZE//4)
        
        # Horns on helmet
        horn_color = (60, 30, 15)
        pygame.draw.polygon(surface, horn_color, [(OBSTACLE_SIZE//3, OBSTACLE_SIZE//6), (OBSTACLE_SIZE//2, OBSTACLE_SIZE//8), (2*OBSTACLE_SIZE//3, OBSTACLE_SIZE//6)])
        
        # Wings (skeletal)
        wing_color = (20, 20, 20)
        pygame.draw.polygon(surface, wing_color, [(0, OBSTACLE_SIZE//2), (OBSTACLE_SIZE//6, OBSTACLE_SIZE//3), (OBSTACLE_SIZE//6, 2*OBSTACLE_SIZE//3)])
        pygame.draw.polygon(surface, wing_color, [(OBSTACLE_SIZE, OBSTACLE_SIZE//2), (5*OBSTACLE_SIZE//6, OBSTACLE_SIZE//3), (5*OBSTACLE_SIZE//6, 2*OBSTACLE_SIZE//3)])
        
        # Staff
        staff_color = (30, 15, 5)
        pygame.draw.rect(surface, staff_color, (OBSTACLE_SIZE//2 - 2, OBSTACLE_SIZE//2, 4, OBSTACLE_SIZE//2))
        
        # Eyes (glowing red)
        pygame.draw.circle(surface, (255, 0, 0), (OBSTACLE_SIZE//3, OBSTACLE_SIZE//3), 3)
        pygame.draw.circle(surface, (255, 0, 0), (2*OBSTACLE_SIZE//3, OBSTACLE_SIZE//3), 3)
    
    def draw_rock_golem(self, surface):
        """Draw the rock golem with stone-like features"""
        # Main body (stone gray)
        body_color = (120, 120, 120)
        pygame.draw.rect(surface, body_color, (OBSTACLE_SIZE//4, OBSTACLE_SIZE//4, OBSTACLE_SIZE//2, 3*OBSTACLE_SIZE//4))
        
        # Head with crown-like crest
        head_color = (100, 100, 100)
        pygame.draw.circle(surface, head_color, (OBSTACLE_SIZE//2, OBSTACLE_SIZE//3), OBSTACLE_SIZE//4)
        
        # Crown crest
        crest_color = (80, 80, 80)
        pygame.draw.polygon(surface, crest_color, [(OBSTACLE_SIZE//3, OBSTACLE_SIZE//6), (OBSTACLE_SIZE//2, OBSTACLE_SIZE//8), (2*OBSTACLE_SIZE//3, OBSTACLE_SIZE//6)])
        
        # Horns on sides
        pygame.draw.polygon(surface, crest_color, [(OBSTACLE_SIZE//6, OBSTACLE_SIZE//4), (OBSTACLE_SIZE//4, OBSTACLE_SIZE//6), (OBSTACLE_SIZE//3, OBSTACLE_SIZE//4)])
        pygame.draw.polygon(surface, crest_color, [(5*OBSTACLE_SIZE//6, OBSTACLE_SIZE//4), (3*OBSTACLE_SIZE//4, OBSTACLE_SIZE//6), (2*OBSTACLE_SIZE//3, OBSTACLE_SIZE//4)])
        
        # Eyes (dark sockets)
        pygame.draw.circle(surface, (20, 20, 20), (OBSTACLE_SIZE//3, OBSTACLE_SIZE//3), 4)
        pygame.draw.circle(surface, (20, 20, 20), (2*OBSTACLE_SIZE//3, OBSTACLE_SIZE//3), 4)
        
        # Mouth with fangs
        pygame.draw.rect(surface, (20, 20, 20), (OBSTACLE_SIZE//3, 2*OBSTACLE_SIZE//3, OBSTACLE_SIZE//3, 3))
        pygame.draw.polygon(surface, (255, 255, 255), [(OBSTACLE_SIZE//3, 2*OBSTACLE_SIZE//3), (OBSTACLE_SIZE//2, 2*OBSTACLE_SIZE//3 - 3), (2*OBSTACLE_SIZE//3, 2*OBSTACLE_SIZE//3)])
        
        # Arms with claws
        arm_color = (110, 110, 110)
        pygame.draw.rect(surface, arm_color, (OBSTACLE_SIZE//6, OBSTACLE_SIZE//2, OBSTACLE_SIZE//6, OBSTACLE_SIZE//3))
        pygame.draw.rect(surface, arm_color, (2*OBSTACLE_SIZE//3, OBSTACLE_SIZE//2, OBSTACLE_SIZE//6, OBSTACLE_SIZE//3))
    
    def draw_werewolf(self, surface):
        """Draw the werewolf with fur and torn jeans"""
        # Main body (brown fur)
        body_color = (139, 69, 19)
        pygame.draw.ellipse(surface, body_color, (OBSTACLE_SIZE//4, OBSTACLE_SIZE//3, OBSTACLE_SIZE//2, 2*OBSTACLE_SIZE//3))
        
        # Head (wolf-like)
        head_color = (160, 82, 45)
        pygame.draw.circle(surface, head_color, (OBSTACLE_SIZE//2, OBSTACLE_SIZE//3), OBSTACLE_SIZE//4)
        
        # Snout
        snout_color = (180, 100, 60)
        pygame.draw.ellipse(surface, snout_color, (OBSTACLE_SIZE//3, OBSTACLE_SIZE//3, OBSTACLE_SIZE//3, OBSTACLE_SIZE//6))
        
        # Ears
        ear_color = (120, 60, 30)
        pygame.draw.ellipse(surface, ear_color, (OBSTACLE_SIZE//4, OBSTACLE_SIZE//6, OBSTACLE_SIZE//8, OBSTACLE_SIZE//6))
        pygame.draw.ellipse(surface, ear_color, (5*OBSTACLE_SIZE//8, OBSTACLE_SIZE//6, OBSTACLE_SIZE//8, OBSTACLE_SIZE//6))
        
        # Eyes (yellow/orange)
        pygame.draw.circle(surface, (255, 165, 0), (OBSTACLE_SIZE//3, OBSTACLE_SIZE//3), 4)
        pygame.draw.circle(surface, (255, 165, 0), (2*OBSTACLE_SIZE//3, OBSTACLE_SIZE//3), 4)
        pygame.draw.circle(surface, (0, 0, 0), (OBSTACLE_SIZE//3, OBSTACLE_SIZE//3), 2)
        pygame.draw.circle(surface, (0, 0, 0), (2*OBSTACLE_SIZE//3, OBSTACLE_SIZE//3), 2)
        
        # Mouth with fangs
        pygame.draw.rect(surface, (0, 0, 0), (OBSTACLE_SIZE//3, 2*OBSTACLE_SIZE//3, OBSTACLE_SIZE//3, 2))
        pygame.draw.polygon(surface, (255, 255, 255), [(OBSTACLE_SIZE//3, 2*OBSTACLE_SIZE//3), (OBSTACLE_SIZE//2, 2*OBSTACLE_SIZE//3 - 2), (2*OBSTACLE_SIZE//3, 2*OBSTACLE_SIZE//3)])
        
        # Arms with claws
        arm_color = (160, 82, 45)
        pygame.draw.rect(surface, arm_color, (OBSTACLE_SIZE//6, OBSTACLE_SIZE//2, OBSTACLE_SIZE//6, OBSTACLE_SIZE//3))
        pygame.draw.rect(surface, arm_color, (2*OBSTACLE_SIZE//3, OBSTACLE_SIZE//2, OBSTACLE_SIZE//6, OBSTACLE_SIZE//3))
        
        # Torn jeans
        jeans_color = (0, 0, 139)
        pygame.draw.rect(surface, jeans_color, (OBSTACLE_SIZE//4, 3*OBSTACLE_SIZE//4, OBSTACLE_SIZE//2, OBSTACLE_SIZE//4))

    def update(self, dt):
        # Obstacles are STATIC - they don't move
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)
