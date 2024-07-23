class Game:
    def __init__(self):
        self.turn = "X"
        self.tie = False
        self.winner = None
        self.board = {
            "a1": None,
            "b1": None,
            "c1": None,
            "a2": None,
            "b2": None,
            "c2": None,
            "a3": None,
            "b3": None,
            "c3": None,
        }

    def play_game(self):
        print("Welcome to Tic Tac Toe")
        while self.winner == None and not self.tie:
            self.render()
            self.get_move()
            self.check_for_winner()
            self.check_for_tie()
            self.switch_turns()
        self.render()

    def print_board(self):
        b = self.board
        print(
            f"""
                A   B   C
            1) {b['a1'] or ' '}  | {b['b1'] or ' '} | {b['c1'] or ' '}
               -----------
            2) {b['a2'] or ' '}  | {b['b2'] or ' '} | {b['c2'] or ' '}
               -----------
            3) {b['a3'] or ' '}  | {b['b3'] or ' '} | {b['c3'] or ' '}
            """
        )

    def print_message(self):
        if self.tie == True:
            print("Tie Game!")
        elif self.winner != None:
            print(f"{self.winner} wins the game!")
        else:
            print(f"It's player {self.turn}'s turn!")

    def render(self):
        self.print_board()
        self.print_message()

    def get_move(self):
        while True:
            move = input(f"Enter a valid move (example: A1): ").lower()
            if move[0] in ["a", "b", "c"] and move[1] in ["1", "2", "3"]:
                break
        self.board[move] = self.turn

    def check_for_winner(self):
        for num in range(1, 4):
            if self.board[f"a{num}"] and (
                self.board[f"a{num}"] == self.board[f"b{num}"] == self.board[f"c{num}"]
            ):
                self.winner = self.turn
        for letter in ["a", "b", "c"]:
            if self.board[f"{letter}1"] and (
                self.board[f"{letter}1"]
                == self.board[f"{letter}2"]
                == self.board[f"{letter}3"]
            ):
                self.winner = self.turn
        if self.board["a1"] and (
            self.board["a1"] == self.board["b2"] == self.board["c3"]
        ):
            self.winner = self.turn
        if self.board["a3"] and (
            self.board["a3"] == self.board["b2"] == self.board["c1"]
        ):
            self.winner = self.turn

    def check_for_tie(self):
        if not None in self.board.values() and self.winner == None:
            self.tie = True

    def switch_turns(self):
        if self.turn == "X":
            self.turn = "O"
        else:
            self.turn = "X"


game_instance = Game()
game_instance.play_game()
