# Game Settings

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GOLD = (255, 215, 0)

# Player settings - ACTUAL Subway Surfers style
PLAYER_FORWARD_SPEED = 400  # Player moves forward at constant speed
PLAYER_JUMP_HEIGHT = 200
PLAYER_GRAVITY = 1000
PLAYER_LANE_CHANGE_SPEED = 800  # Even smoother lane changes
PLAYER_SIZE = 50

# Lane positions - 5 lanes for full horizontal space
LANE_WIDTH = 120
LANE_POSITIONS = [
    SCREEN_WIDTH // 2 - (LANE_WIDTH * 2),  # Far left
    SCREEN_WIDTH // 2 - LANE_WIDTH,         # Left
    SCREEN_WIDTH // 2,                       # Center  
    SCREEN_WIDTH // 2 + LANE_WIDTH,         # Right
    SCREEN_WIDTH // 2 + (LANE_WIDTH * 2)    # Far right
]

# Obstacle settings - obstacles are STATIC, player moves past them
OBSTACLE_SPAWN_INTERVAL = 600  # milliseconds (faster spawning for more obstacles)
OBSTACLE_SIZE = 60

# Power-up settings
POWERUP_DURATION = 5000  # milliseconds
POWERUP_SPAWN_INTERVAL = 1500  # milliseconds (more frequent since no normal coins)
POWERUP_SIZE = 60  # Bigger size for better visibility

# Game settings
LEVEL1_DISTANCE = 60  # meters for first level (1 minute at current speed)
LEVEL2_DISTANCE = 120  # meters for second level (2 minutes at current speed)
GAME_DURATION = 180  # seconds (3 minutes total)
DISTANCE_PER_SECOND = LEVEL2_DISTANCE / GAME_DURATION  # meters per second

# Game states
GAME_STATE_MENU = 0
GAME_STATE_PLAYING = 1
GAME_STATE_GAME_OVER = 2
GAME_STATE_INTRO = 3
GAME_STATE_LEVEL_COMPLETE = 4

# Audio settings - Reduced volumes for less annoying sounds
VOLUME_MUSIC = 0.3
VOLUME_SFX = 0.2



