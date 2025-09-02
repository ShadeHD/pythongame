# Justin's Dash for Love - Subway Surfers Style Runner

A redesigned endless runner game inspired by Subway Surfers where you control Justin as he runs through obstacles to reach his goal.

## Game Overview

- **Objective**: Complete 2 levels - Level 1 (50m) then Level 2 (100m total)
- **Style**: Subway Surfers-style 5-lane running game
- **Controls**: Smooth and intuitive movement system
- **Visuals**: Refined characters and monster-like obstacles

## How to Play

### Controls
- **Arrow Keys** or **A/D**: Move left and right between 5 lanes
- **Space** or **Up Arrow**: Jump over obstacles
- **Down Arrow**: Slide under obstacles
- **Enter**: Start game from menu
- **R**: Restart game after game over
- **Q**: Quit game

### Gameplay
1. **Start**: Press Enter on the main menu to begin
2. **Level 1**: Run 50 meters through park obstacles
3. **Level Complete**: See completion message and continue to Level 2
4. **Level 2**: Run additional 50 meters through industrial obstacles
5. **Victory**: Complete both levels to win!

### Power-ups
- **Coins**: Collect for points
- **Shield**: Temporary invincibility (blue circle)
- **Magnet**: Attracts nearby power-ups (green circle)
- **Speed Boost**: Increases movement speed (red lines)

### Game States
- **Level 1**: Park environment with bench/trash obstacles
- **Level Complete**: Celebration screen between levels
- **Level 2**: Industrial environment with crate/pipe obstacles
- **Victory**: Complete both levels - you win!
- **Game Over**: Hit an obstacle or run out of time

## Features

### Two-Level System
- **Level 1**: 50 meters through park environment
- **Level Complete**: Celebration screen with score
- **Level 2**: Additional 50 meters through industrial environment
- **Total Goal**: 100 meters across both levels

### Visual Improvements
- **Refined Characters**: Background removed, cleaner appearance
- **Monster Obstacles**: Darkened, more menacing appearance
- **5-Lane Movement**: Full horizontal space utilization
- **Smooth Movement**: Ultra-responsive controls
- **Progress Tracking**: Clear level and distance indicators

### Technical Improvements
- **Smoother Controls**: Faster lane changes and movement
- **Better Collision Detection**: More accurate obstacle avoidance
- **Optimized Performance**: Smooth 60 FPS gameplay
- **Level Progression**: Clear level completion system

## Installation and Running

1. **Requirements**: Python 3.x and Pygame
2. **Install Pygame**: `pip install pygame`
3. **Run Game**: `python main.py` or `py main.py`

## Game Structure

- **Menu State**: Main menu with game title and instructions
- **Intro State**: Brief tutorial and controls explanation
- **Playing State**: Main gameplay with level progression
- **Level Complete State**: Celebration between levels
- **Game Over State**: Results screen with restart option

## Tips for Success

1. **Use All Lanes**: 5 lanes give you more options
2. **Watch Level Progress**: Each level has different obstacles
3. **Collect Power-ups**: They provide valuable bonuses
4. **Practice Movement**: Smooth controls become natural
5. **Plan Ahead**: Look for upcoming obstacles

## Technical Details

- **Engine**: Pygame
- **Resolution**: 800x600
- **FPS**: 60
- **Level 1**: 50 meters
- **Level 2**: 100 meters total
- **Time Limit**: 120 seconds (2 minutes)
- **Lanes**: 5 (full horizontal space)

Enjoy the game! Run, jump, slide, and complete both levels to win!
