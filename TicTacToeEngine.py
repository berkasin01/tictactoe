from tabulate import tabulate
import numpy


class TicTacToe:
    def __init__(self):
        self.head = ["A", "B", "C"]
        self.table = [["", "", ""],
                      ["", "", ""],
                      ["", "", ""]
                      ]
        self.make_table = tabulate(self.table, tablefmt="heavy_grid", headers=self.head, showindex=True)
        self.turn = 1
        self.input = ""
    def get_user_input(self):
        self.turn += 1
        print(self.make_table)
        if self.turn % 2 == 0:
            self.input = "X"
        else:
            self.input = "O"
        print(f"It is {self.input}'s turn")
        take_turn = input("Pick an area?")
        user = list(take_turn)
        row_value = int(self.head.index(user[0]))
        column_val = int(user[1])
        self.table[column_val][row_value] = self.input
        self.make_table = tabulate(self.table, tablefmt="heavy_grid", headers=self.head, showindex=True)

    def check_winner(self):
        for rows in self.table:
            if rows == ["X", "X", "X"]:
                print("X Wins!")
            elif rows == ["O", "O", "O"]:
                print("O Wins")



