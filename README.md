# Battleship Game
This project is a simple command-line implementation of the classic Battleship game. The game is designed for two players who take turns to place their ships on the board and then attempt to guess the location of the opponent's ships.

## Features
- Player vs Player: Two players can play against each other.
- Customizable Ship Placement: Players can manually input the positions of their ships on the board.
- Game Logic: The game checks for hits and misses, updates the board, and announces the winner when all ships are sunk.
- Input Validation: Ensures that player inputs are valid and that ships are placed correctly on the board.

## How to Play
- Setup: Each player enters their name and places their ships on a 7x7 grid. There are three types of ships: 1 Submarine (3 fields), 2 Destroyers (2 fields each) and 3 Patrol Boats (1 field each).
- Gameplay: Players take turns to shoot at each other's grids by inputting a field (e.g., "A3"). The game informs whether the shot was a hit or a miss (a hit is marked with the symbol ■ and a miss is marked with the symbol ×). The board is updated after each shot to reflect the current state of the game.
- Winning: A player wins by successfully hitting all the fields occupied by their opponent's ships.
