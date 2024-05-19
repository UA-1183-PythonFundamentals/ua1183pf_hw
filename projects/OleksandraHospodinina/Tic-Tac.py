import tkinter as tk
from tkinter import messagebox
import random


class TicTac:
    def __init__(self, root):
        """
        Initializes the TicTacToe game.
        :param root: The root window object of Tkinter.
        """
        self.root = root
        self.root.title("Tic Tac")
        self.board = [None] * 9
        self.current_player = None
        self.user_symbol = None
        self.computer_symbol = None
        self.buttons = []
        self.create_start_screen()

    def create_start_screen(self):
        """
        Creates the start screen where the user can choose their symbol (X or O).
        """
        self.start_frame = tk.Frame(self.root)
        self.start_frame.pack()

        tk.Label(self.start_frame, text="Choose your symbol", font=('normal', 20)).pack()

        tk.Button(self.start_frame, text="X", font=('normal', 20), command=lambda: self.start_game("X")).pack(
            side=tk.LEFT, padx=20)
        tk.Button(self.start_frame, text="O", font=('normal', 20), command=lambda: self.start_game("O")).pack(
            side=tk.RIGHT, padx=20)

    def start_game(self, symbol):
        """
        Starts the game with the user's choice of symbol.
        :param symbol: The symbol chosen by the user (X or O).
        """
        self.user_symbol = symbol
        self.computer_symbol = "O" if symbol == "X" else "X"
        self.current_player = "X"
        self.start_frame.destroy()
        self.create_board()

    def create_board(self):
        """
        Creates the Tic-Tac-Toe game board.
        """
        for i in range(9):
            button = tk.Button(self.root, text="", font=('normal', 20, 'normal'), height=3, width=6,
                               command=lambda i=i: self.on_button_click(i))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

        # If the computer is "X", it makes the first move
        if self.computer_symbol == "X":
            self.computer_move()

    def on_button_click(self, index):
        """
        Handles the button click event for the user's move.
        :param index: The index of the button clicked by the user.
        """
        if self.board[index] is None and self.current_player == self.user_symbol:
            self.make_move(index, self.user_symbol)
            if not self.check_winner() and not all(self.board):
                self.current_player = self.computer_symbol
                self.computer_move()

    def computer_move(self):
        """
        Handles the computer's move by selecting a random available position.
        """
        available_moves = [i for i, x in enumerate(self.board) if x is None]
        index = random.choice(available_moves)
        self.make_move(index, self.computer_symbol)
        if not self.check_winner() and not all(self.board):
            self.current_player = self.user_symbol

    def make_move(self, index, player):
        """
        Makes a move on the board.
        :param index: The index on the board where the move is made.
        :param player: The player making the move (user or computer).
        """
        self.board[index] = player
        self.buttons[index].config(text=player)
        if self.check_winner():
            messagebox.showinfo("Tic Tac", f"Player {player} wins!")
            self.reset_board()
        elif all(self.board):
            messagebox.showinfo("Tic Tac", "It's a tie!")
            self.reset_board()

    def check_winner(self):
        """
        Checks if there is a winner on the board.
        :return: True if there is a winner, False otherwise.
        """
        win_positions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]
        for pos in win_positions:
            if self.board[pos[0]] == self.board[pos[1]] == self.board[pos[2]] == self.current_player:
                return True
        return False

    def reset_board(self):
        """
        Resets the game board for a new game.
        """
        self.board = [None] * 9
        for button in self.buttons:
            button.config(text="")
        self.current_player = "X"
        if self.computer_symbol == "X":
            self.computer_move()


if __name__ == "__main__":
    root = tk.Tk()
    game = TicTac(root)
    root.mainloop()
