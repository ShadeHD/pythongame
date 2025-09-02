import pygame
import random
from settings import *
from obstacle import Obstacle
from monster_obstacles import MonsterObstacle
from powerup import PowerUp

class LevelManager:
    def __init__(self, asset_loader):
        self.asset_loader = asset_loader
        self.obstacles = pygame.sprite.Group()
        self.powerups = pygame.sprite.Group()
        self.last_obstacle_spawn_time = pygame.time.get_ticks()
        self.last_powerup_spawn_time = pygame.time.get_ticks()
        self.obstacle_spawn_interval = OBSTACLE_SPAWN_INTERVAL
        self.game_start_time = pygame.time.get_ticks()
        self.distance = 0
        self.player_forward_speed = PLAYER_FORWARD_SPEED
        self.current_level = 1
        self.level_completed = False
        self.update_obstacle_spawn_rate()

    def update(self, dt):
        self.spawn_obstacles()
        self.spawn_powerups()
        
        # Update distance based on player's forward movement
        self.distance += self.player_forward_speed * dt / 100  # Convert to meters
        
        # Remove obstacles that are far behind the player
        for obstacle in self.obstacles:
            if obstacle.rect.y > SCREEN_HEIGHT + 100:
                obstacle.kill()
                
        # Remove powerups that are far behind the player
        for powerup in self.powerups:
            if powerup.rect.y > SCREEN_HEIGHT + 100:
                powerup.kill()

    def draw(self, screen):
        self.obstacles.draw(screen)
        self.powerups.draw(screen)

    def spawn_obstacles(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_obstacle_spawn_time > self.obstacle_spawn_interval:
            # Spawn 1-2 obstacles for level 1, 1-2 obstacles for level 2 (easier)
            num_obstacles = random.randint(1, 2) if self.current_level == 1 else random.randint(1, 2)
            
            for _ in range(num_obstacles):
                # Choose random monster obstacle
                monster_type = random.choice(["monster1", "monster2", "monster3"])
                
                # Choose a random lane for the obstacle
                lane_index = random.randint(0, len(LANE_POSITIONS) - 1)
                lane_x = LANE_POSITIONS[lane_index]
                y = -OBSTACLE_SIZE - random.randint(0, 50)  # Spawn off-screen above with some variation
                
                obstacle = MonsterObstacle(monster_type, lane_x - OBSTACLE_SIZE // 2, y)
                self.obstacles.add(obstacle)
            
            self.last_obstacle_spawn_time = current_time

    def spawn_powerups(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_powerup_spawn_time > POWERUP_SPAWN_INTERVAL:
            # Love-themed power-ups only (no normal coins)
            powerup_type = random.choice(["kiss", "love_hug", "couple", "love_call"])
            
            # Choose a random lane for the power-up
            lane_index = random.randint(0, len(LANE_POSITIONS) - 1)
            lane_x = LANE_POSITIONS[lane_index]
            y = random.randint(-100, -50)  # Spawn off-screen above
            
            powerup = PowerUp(self.asset_loader, lane_x - POWERUP_SIZE // 2, y, powerup_type, POWERUP_DURATION)
            self.powerups.add(powerup)
            self.last_powerup_spawn_time = current_time

    def check_level_completion(self):
        """Check if current level is completed"""
        if self.current_level == 1 and self.distance >= LEVEL1_DISTANCE:
            return True
        elif self.current_level == 2 and self.distance >= LEVEL2_DISTANCE:
            return True
        return False

    def check_game_completion(self):
        # Check if player has completed both levels
        return self.current_level == 2 and self.distance >= LEVEL2_DISTANCE

    def check_game_timeout(self):
        # Check if 2 minutes have passed
        current_time = pygame.time.get_ticks()
        return (current_time - self.game_start_time) / 1000 >= GAME_DURATION

    def get_remaining_time(self):
        current_time = pygame.time.get_ticks()
        elapsed = (current_time - self.game_start_time) / 1000
        return max(0, GAME_DURATION - elapsed)

    def get_progress_percentage(self):
        if self.current_level == 1:
            return min(100, (self.distance / LEVEL1_DISTANCE) * 100)
        else:
            return min(100, ((self.distance - LEVEL1_DISTANCE) / (LEVEL2_DISTANCE - LEVEL1_DISTANCE)) * 100)

    def get_target_distance(self):
        if self.current_level == 1:
            return LEVEL1_DISTANCE
        else:
            return LEVEL2_DISTANCE

    def start_level_2(self):
        """Start level 2"""
        self.current_level = 2
        self.level_completed = False
        self.distance = 0  # Reset distance for level 2
        self.obstacles.empty()
        self.powerups.empty()
        self.update_obstacle_spawn_rate()
    
    def update_obstacle_spawn_rate(self):
        """Update obstacle spawn rate based on current level"""
        if self.current_level == 1:
            self.obstacle_spawn_interval = 600  # 0.6 seconds for level 1
        else:  # Level 2
            self.obstacle_spawn_interval = 700  # 0.7 seconds for level 2 (easier)

    def reset(self):
        self.obstacles.empty()
        self.powerups.empty()
        self.last_obstacle_spawn_time = pygame.time.get_ticks()
        self.last_powerup_spawn_time = pygame.time.get_ticks()
        self.obstacle_spawn_interval = OBSTACLE_SPAWN_INTERVAL
        self.game_start_time = pygame.time.get_ticks()
        self.distance = 0
        self.current_level = 1
        self.level_completed = False

