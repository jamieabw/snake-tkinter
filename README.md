# snake-tkinter
A basic snake game made using tkinter.
This is a classic Snake game implemented in Python using the Tkinter library for the graphical user interface. The objective of the game is to control the snake to eat fruits and grow longer without colliding with the boundaries of the game window or with its own body.

## How to Play
Use the W, A, S, D keys to change the direction of the snake.
The game starts with an initial length of 3 segments, represented by green rectangles.
The score is displayed at the bottom of the game window.
The snake grows longer and the score increases when it eats a fruit, represented by a red rectangle.
The game ends if the snake collides with the boundaries of the game window or with its own body.

## Game Configuration
The game has several constants that can be adjusted for different game experiences. These constants are stored at the beginning of the code and include:

GAME_HEIGHT: The height of the game window in pixels.
GAME_WIDTH: The width of the game window in pixels.
GRID_SIZE: The size of each grid square in pixels.
INITIAL_LENGTH: The initial length of the snake in segments.
MOVEMENT_DELAY: The delay between each movement of the snake in milliseconds.
