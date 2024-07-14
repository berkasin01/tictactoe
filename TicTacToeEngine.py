from tabulate import tabulate

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
        self.winner_combs = [
            [[0, 0], [1, 0], [2, 0]],
            [[0, 1], [1, 1], [2, 1]],
            [[0, 2], [1, 2], [2, 2]],
            [[0, 2], [1, 1], [2, 0]],
            [[0, 0], [1, 1], [2, 2]],
        ]
        self.x_locations = []
        self.o_locations = []
        self.demo = []
        self.all_input = []
        print(self.make_table)

    def take_go(self):
        self.turn += 1
        if self.turn % 2 == 0:
            self.input = "X"
            self.get_user_input()
            self.x_locations.append(self.demo)
            print(self.make_table)
            if self.check_winner():
                print("X WINS!")
                return False
            else:
                return True
        else:
            self.input = "O"
            self.get_user_input()
            self.o_locations.append(self.demo)
            print(self.make_table)
            if self.check_winner():
                print("Y WINS!")
                return False
            else:
                return True

    def get_user_input(self):
        print(f"It is {self.input}'s turn")
        take_turn = input("Pick an area?")
        user = list(take_turn)
        user[0] = user[0].upper()
        if user[0] in self.head and user[1] in ["0", "1", "2"] and len(user) == 2 and user not in self.all_input:
            self.all_input.append(user)
            row_value = int(self.head.index(user[0]))
            column_val = int(user[1])
            self.demo = [column_val, row_value]
            self.table[column_val][row_value] = self.input
            self.make_table = tabulate(self.table, tablefmt="heavy_grid", headers=self.head, showindex=True)
        else:
            self.turn -= 1
            print("Not available input, Please Try Again!")

    def check_winner(self):
        for rows in self.table:
            if rows == ["X", "X", "X"] or rows == ["O", "O", "O"]:
                return True
        for winners in self.winner_combs:
            if self.x_locations == winners or self.o_locations == winners:
                return True
