# Snake Game

This is a Python-based Snake game built using the `pygame` library.

## Features

- **Snake Movement**:

  - Control the snake using the arrow keys.
  - Movement restrictions prevent the snake from reversing directly into itself (e.g., moving left after moving right).

- **Gameplay**:

  - The snake grows longer each time it eats food.
  - The game ends if the snake collides with itself or the screen boundaries.

- **Score Tracking**:

  - The score increases as the snake eats more food.
  - The current score is displayed at the top of the screen.

- **Game Over Options**:
  - After losing, players can restart the game by pressing `C` or quit by pressing `Q`.

## Requirements

- Python 3.6 or later
- `pygame` library

## Installation

1. Clone or download this repository.
2. Ensure you have the `requirements.txt` file in the project directory.

3. Set up a virtual environment (optional but recommended):
   ```bash
   python -m venv snake_game_env
   source snake_game_env/bin/activate  # On Windows, use snake_game_env\Scripts\activate
   ```
4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## How to Run

1. Save the game script as `snake_game.py`.
2. Run the script:
   ```bash
   python snake_game.py
   ```

## Gameplay Instructions

- Use the arrow keys to move the snake.
- Eat the red food to grow longer and increase your score.
- Avoid colliding with the edges of the screen or yourself.
- When the game ends:
  - Press `C` to restart.
  - Press `Q` to quit.

## License

This project is provided as-is for educational purposes. Feel free to modify and improve it!
