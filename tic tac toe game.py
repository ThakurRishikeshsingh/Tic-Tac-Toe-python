import math
import random
import tkinter as tk
from tkinter import messagebox


class TicTacToe:

    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe vs Unbeatable AI")
        self.root.geometry("450x500")
        self.root.resizable(False, False)
        self.root.configure(bg="#2c3e50")

        # Game variables
        self.board = [" " for _ in range(9)]  # 3x3 board representation
        self.human = "X"
        self.ai = "O"
        self.current_player = "X"  # Human goes first

        # Setup GUI elements
        self.create_widgets()

    def create_widgets(self):
        """Creates the grid layout and header labels."""
        # Header Label
        self.header_label = tk.Label(
            self.root,
            text="Your Turn (X)",
            font=("Arial", 16, "bold"),
            bg="#2c3e50",
            fg="#ecf0f1",
        )
        self.header_label.pack(pady=15)

        # Container Frame for the Grid
        self.grid_frame = tk.Frame(self.root, bg="#34495e", bd=4, relief="ridge")
        self.grid_frame.pack(pady=5)

        # Buttons grid setup
        self.buttons = []
        for i in range(9):
            row = i // 3
            col = i % 3
            btn = tk.Button(
                self.grid_frame,
                text="",
                font=("Arial", 24, "bold"),
                width=5,
                height=2,
                bg="#ecf0f1",
                activebackground="#bdc3c7",
                command=lambda idx=i: self.human_move(idx),
            )
            btn.grid(row=row, column=col, padx=4, pady=4)
            self.buttons.append(btn)

        # Reset button at the bottom
        reset_btn = tk.Button(
            self.root,
            text="Restart Match",
            font=("Arial", 12, "bold"),
            bg="#e74c3c",
            fg="white",
            activebackground="#c0392b",
            activeforeground="white",
            padx=10,
            pady=5,
            command=self.reset_game,
        )
        reset_btn.pack(pady=20)

    def human_move(self, index):
        """Handles human interaction and hands off turn to AI."""
        if self.board[index] == " " and self.current_player == self.human:
            self.make_move(index, self.human)

            if not self.check_game_over():
                self.current_player = self.ai
                self.header_label.config(text="AI is thinking...", fg="#f1c40f")
                # Let the GUI refresh before the AI runs its calculation
                self.root.after(400, self.ai_move)

    def ai_move(self):
        """Finds the perfect move using Minimax and executes it."""
        best_score = -math.inf
        best_move = None

        # Loop through all available empty cells
        for i in range(9):
            if self.board[i] == " ":
                self.board[i] = self.ai
                score = self.minimax(self.board, 0, False)
                self.board[i] = " "  # Undo move simulation

                if score > best_score:
                    best_score = score
                    best_move = i

        if best_move is not None:
            self.make_move(best_move, self.ai)

        if not self.check_game_over():
            self.current_player = self.human
            self.header_label.config(text="Your Turn (X)", fg="#ecf0f1")

    def minimax(self, board, depth, is_maximizing):
        """Core recursive Minimax function evaluating the game tree."""
        # Base terminal cases evaluation
        if self.check_winner(self.ai):
            return 10 - depth  # Prioritize faster wins
        if self.check_winner(self.human):
            return depth - 10  # Prioritize stalling losses
        if " " not in board:
            return 0  # Tie

        if is_maximizing:
            best_score = -math.inf
            for i in range(9):
                if board[i] == " ":
                    board[i] = self.ai
                    score = self.minimax(board, depth + 1, False)
                    board[i] = " "
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = math.inf
            for i in range(9):
                if board[i] == " ":
                    board[i] = self.human
                    score = self.minimax(board, depth + 1, True)
                    board[i] = " "
                    best_score = min(score, best_score)
            return best_score

    def make_move(self, index, player):
        """Updates board list tracking state and updates visual buttons."""
        self.board[index] = player
        color = "#3498db" if player == "X" else "#2ecc71"
        self.buttons[index].config(text=player, state="disabled", disabledforeground=color)

    def check_winner(self, player):
        """Checks rows, columns, and diagonals for a winning line."""
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]             # Diagonals
        ]
        return any(all(self.board[i] == player for i in condition) for condition in win_conditions)

    def check_game_over(self):
        """Checks for endings and throws prompt alerts."""
        if self.check_winner(self.human):
            self.end_match("Congratulations!", "You beat the bot! (This shouldn't happen)")
            return True
        if self.check_winner(self.ai):
            self.end_match("Defeat!", "The AI won! Try working on defense.")
            return True
        if " " not in self.board:
            self.end_match("Draw!", "It's a perfect tie game!")
            return True
        return False

    def end_match(self, title, announcement):
        self.header_label.config(text=title, fg="#e74c3c")
        messagebox.showinfo(title, announcement)

    def reset_game(self):
        """Clears board data states back to blank initialization."""
        self.board = [" " for _ in range(9)]
        self.current_player = self.human
        self.header_label.config(text="Your Turn (X)", fg="#ecf0f1")
        for btn in self.buttons:
            btn.config(text="", state="normal", bg="#ecf0f1")


if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
