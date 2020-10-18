from player import Player
from random import choice


class RandomPlayer(Player):
    def __init__(self):
        super().__init__()

    def move(self) -> str:
        """
        Overrides default player that always throws 'rock'
        Returns a random move in string format. Example:
        'rock', 'paper', or 'scissors'
        """
        return choice(self.VALID_MOVES)
