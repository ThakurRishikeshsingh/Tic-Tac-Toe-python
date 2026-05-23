# Unbeatable Tic-Tac-Toe AI

An interactive Desktop GUI Tic-Tac-Toe game built in Python using `tkinter`. It features an AI opponent running on the **Minimax Algorithm**, making it mathematically impossible to defeat. 

---

## How to Play

1. Run the script to open the application window.
2. You play as **X** and always get the first move.
3. Click any empty square on the 3x3 grid to place your token.
4. The AI (**O**) will calculate its best response almost instantly.
5. If you make a mistake, the AI will capitalize and win. If you play perfectly, the match will result in a tie!

---

## Technical Details: The Minimax Engine

The AI uses a recursive game-theory formula called **Minimax** to evaluate every possible future outcome on the board. 

- **Maximizing state (+10):** The AI searches for paths leading to its own victory.
- **Minimizing state (-10):** The AI assumes you will play perfectly to stop it, scoring your winning layouts at the lowest value.
- **Depth Penalty:** The algorithm prioritizes immediate wins over delayed wins by factoring in a depth deduction ($10 - \text{depth}$).

---

## Installation & Running

No external packages or `pip install` commands are required.

```bash
# Clone the repository
git clone [https://github.com/ThakurRishikehsingh/unbeatable-tic-tac-toe.git](https://github.com/ThakurRishikeshsingh/unbeatable-tic-tac-toe.git)

# Navigate into the project folder
cd unbeatable-tic-tac-toe

# Run the game
python tic_tac_toe.py