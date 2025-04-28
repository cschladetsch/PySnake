# Snake Game

A classic Snake game implemented in Python using Pygame.

## Demo

[Demo](resources/Demo.gif)

## Description

This is a simple implementation of the classic Snake game. The player controls a snake that moves around the screen, eating food to grow longer. The game ends if the snake collides with the walls or with itself.

## Features

- Smooth snake movement
- Score tracking
- Food spawns randomly on the grid
- Toggle between wall collision mode and wrap-around mode
- Start screen with instructions
- Game over screen with restart option
- Gradual speed increase as the snake grows
- Visual grid for better spatial awareness

## Prerequisites

Before you can run this game, you need to have Python and Pygame installed on your system.

```
pip install pygame
```

## How to Play

1. Clone or download this repository
2. Run the game:
   ```
   python main.py
   ```
3. Use the arrow keys to control the snake:
   - Up arrow: Move up
   - Down arrow: Move down
   - Left arrow: Move left
   - Right arrow: Move right
4. Try to eat the red food items to grow your snake and increase your score
5. Avoid hitting the walls or running into your own tail

## Game Controls

- **Arrow Keys**: Control the snake's direction
- **SPACE**: Toggle wall collisions (on start screen) / Restart game (on game over screen)
- **ENTER**: Start the game from the start screen
- **P**: Pause/unpause the game during gameplay
- **Close Window**: Quit the game

## Technical Details

- Written in Python 3
- Uses Pygame for graphics and input handling
- Fixed grid-based movement
- 10 frames per second gameplay speed

### Common Warnings

When running the game, you may see warnings like:

```
RuntimeWarning: Your system is avx2 capable but pygame was not built with support for it.
```

Or ALSA-related warnings on Linux systems:

```
ALSA lib confmisc.c:855:(parse_card) cannot find card '0'
ALSA lib conf.c:5204:(_snd_config_evaluate) function snd_func_card_inum returned error: No such file or directory
```

These warnings are common and typically don't affect gameplay. The game should run normally despite these messages.

## Project Structure

```
snake-game/
³
ÃÄÄ main.py        # Main game file with Snake and Food classes
ÀÄÄ README.md      # This file
```

## Future Improvements

Possible enhancements for future versions:
- Add a high score system
- Implement different difficulty levels
- Add sound effects
- Create start and game over screens
- Add obstacles or power-ups

## License

This project is open source and available for anyone to use and modify.

## Acknowledgments

- Inspired by the classic Snake game
- Built with Pygame (https://www.pygame.org/)
