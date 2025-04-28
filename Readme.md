# Snake Game

A classic Snake game implemented in Python using Pygame.

## Description

This is a simple implementation of the classic Snake game. The player controls a snake that moves around the screen, eating food to grow longer. The game ends if the snake collides with the walls or with itself.

## Features

- Smooth snake movement
- Score tracking
- Food spawns randomly on the grid
- Game over on collision with walls or self

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
- **Close Window**: Quit the game

## Technical Details

- Written in Python 3
- Uses Pygame for graphics and input handling
- Fixed grid-based movement
- 10 frames per second gameplay speed

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
