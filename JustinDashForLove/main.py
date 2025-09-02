import pygame
import sys
from settings import *
from asset_loader import AssetLoader
from player import Player
from level_manager import LevelManager
from sound_manager import SoundManager
from game_state_manager import GameStateManager

# Initialize Pygame
pygame.init()
pygame.font.init()

# Initialize mixer
try:
    pygame.mixer.init()
    print("Audio system initialized successfully")
except pygame.error as e:
    print(f"Could not initialize audio: {e}")

# Set up the display FIRST
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Justin's Dash for Love")

# Asset Loader
asset_loader = AssetLoader()

# Load assets
print("Loading game assets...")
asset_loader.load_image('assets/images/characters/justin.png', 'justin')
asset_loader.load_image('assets/images/characters/sehba.png', 'sehba')
asset_loader.load_image('assets/images/backgrounds/level1_park.png', 'level1_park_bg')
asset_loader.load_image('assets/images/backgrounds/level2_industrial.png', 'level2_industrial_bg')
asset_loader.load_image('assets/images/obstacles/park_bench.png', 'park_bench')
asset_loader.load_image('assets/images/obstacles/trash_can.png', 'trash_can')
asset_loader.load_image('assets/images/obstacles/industrial_crate.png', 'industrial_crate')
asset_loader.load_image('assets/images/obstacles/pipe.png', 'pipe')
asset_loader.load_image('assets/images/powerups/shield.png', 'shield')
asset_loader.load_image('assets/images/powerups/speed_boost.png', 'speed_boost')

# Load only essential sounds - NO JUMP OR SLIDE SOUNDS
asset_loader.load_sound('assets/audio/level1_music.mp3', 'level1_music')
asset_loader.load_sound('assets/audio/level2_music.mp3', 'level2_music')
asset_loader.load_sound('assets/audio/drop-coin-384921.mp3', 'coin_sfx')
asset_loader.load_sound('assets/audio/collision.mp3', 'collision_sfx')

print("Initializing game components...")
# Game objects
sound_manager = SoundManager(asset_loader)
game_state_manager = GameStateManager(GAME_STATE_MENU, asset_loader, sound_manager)

print("Starting game loop...")
# Game loop
running = True
clock = pygame.time.Clock()

try:
    while running:
        dt = clock.tick(FPS) / 1000.0  # Delta time in seconds

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            game_state_manager.handle_input(event)  # Let state manager handle input

        # Update game logic based on state
        game_state_manager.update(dt)

        # Drawing
        game_state_manager.draw(SCREEN)

        pygame.display.flip()

except Exception as e:
    print(f"Game error: {e}")
    import traceback
    traceback.print_exc()

finally:
    pygame.quit()
    sys.exit()


