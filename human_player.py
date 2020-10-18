from player import Player


class HumanPlayer(Player):
    def __init__(self):
        super().__init__()

    def move(self) -> str:
        return self._get_valid_move()

    def _get_valid_move(self) -> str:
        print("['rock', 'paper', 'scissors']")
        move = input("Make a move: ")
        if move not in self.VALID_MOVES:
            while True:
                move = input("\nInvalid move. Usage: "
                             "['rock', 'paper', 'scissors']\n"
                             "Try again: ")
                if move in self.VALID_MOVES:
                    break
        return move
