# Dodging a planet GAME

![bandicam 2023-03-14 13-03-35-980 mp4_000006966](https://user-images.githubusercontent.com/116435847/224890349-27c8e5d5-7146-4508-ae7c-b953e844fea7.gif)

This is a simple game created using the Pygame library in Python. The game is called "UG Spaceman dodging a falling planet". In the game, the player controls a character represented by an image, which can move left and right on the screen using the arrow keys. The objective is to avoid getting hit by falling objects represented by another image, which continuously fall from the top of the screen.

The game window size is 400x400 pixels and it displays a background image, a character image, and an enemy image. The background image is fixed, while the character and enemy images move independently. The enemy image falls at a constant rate, and if it reaches the bottom of the screen without colliding with the character, a new enemy image is generated at a random x-coordinate at the top of the screen.

The game ends if the character collides with an enemy image. Once the game is over, the Pygame window is closed.
