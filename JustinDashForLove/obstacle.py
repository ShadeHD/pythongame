import pygame
from settings import *

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()
        self.image = pygame.transform.scale(image, (OBSTACLE_SIZE, OBSTACLE_SIZE))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.original_y = y  # Store original Y position

    def update(self, dt):
        # Obstacles are STATIC - they don't move
        # The player moves forward past them
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)


