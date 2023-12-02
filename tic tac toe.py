import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Крестики-нолики")
        self.current_player = "X"
        self.board = [[" " for _ in range(3)] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                button = tk.Button(self.window, text=" ", font=("Helvetica", 24), width=6, height=3,
                                   command=lambda row=i, col=j: self.make_move(row, col))
                button.grid(row=i, column=j)

    def make_move(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            self.update_button(row, col)

            if self.check_winner():
                messagebox.showinfo("Победа", f"Игрок {self.current_player} победил!")
                self.reset_board()
            elif self.is_board_full():
                messagebox.showinfo("Ничья", "Игра завершена ничьей!")
                self.reset_board()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def update_button(self, row, col):
        button = self.window.grid_slaves(row=row, column=col)[0]
        button.config(text=self.current_player, state=tk.DISABLED)

    def check_winner(self):
        for i in range(3):
            if all(self.board[i][j] == self.current_player for j in range(3)) or all(
                    self.board[j][i] == self.current_player for j in range(3)):
                return True

        if all(self.board[i][i] == self.current_player for i in range(3)) or all(
                self.board[i][2 - i] == self.current_player for i in range(3)):
            return True

        return False

    def is_board_full(self):
        return all(self.board[i][j] != " " for i in range(3) for j in range(3))

    def reset_board(self):
        for i in range(3):
            for j in range(3):
                button = self.window.grid_slaves(row=i, column=j)[0]
                button.config(text=" ", state=tk.NORMAL)
                self.board[i][j] = " "
        self.current_player = "X"

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()
