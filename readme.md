# Towers of Hanoi Game

## Introduction

This is a terminal-based Towers of Hanoi game implemented in Python. The game allows players to move disks between three stacks, following the classic Towers of Hanoi rules. The objective is to move all disks from the leftmost stack to the rightmost stack in the fewest possible moves.

## How to Play

1. Run the script in the terminal:
   ```sh
   python3 script.py
   ```
2. Enter the number of disks (minimum of 3) when prompted.
3. The game will display the optimal number of moves required.
4. Choose a stack to move from and a stack to move to by entering the corresponding letters.
5. Continue moving disks while following the Towers of Hanoi rules:
   - A larger disk cannot be placed on top of a smaller disk.
   - Only one disk can be moved at a time.
6. The game ends when all disks are successfully moved to the rightmost stack.

## Requirements

- Python 3.x

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/rrugile/hanoi_towers.git
   ```
2. Navigate to the project directory:
   ```sh
   cd hanoi_towers
   ```
3. Run the game:
   ```sh
   python3 script.py
   ```

## File Structure

```
├── node.py   # Defines the Node class for linked list implementation
├── script.py # Main game script
├── stack.py  # Implements the Stack class for managing disk movements
```

## Future Improvements

- Implement a GUI
- Add difficulty levels
- Allow multiplayer mode
