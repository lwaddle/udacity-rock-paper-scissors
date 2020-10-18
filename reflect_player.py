from player import Player
from random import choice


class ReflectPlayer(Player):
    """
    Subclass of Player that remembers what move the opponent played
    last round, and plays that move this round. (In other words, if
    you play 'paper' on the first round, a ReflectPlayer will
    play 'paper' on the second round.) First round will throw a random.
    """

    def __init__(self):
        super().__init__()

    def move(self):
        # Throw a random on the first move
        # then throw a reflection of the previous player's
        # throw.
        if self.last_move_opponent not in self.VALID_MOVES:
            return choice(self.VALID_MOVES)
        else:
            return self.last_move_opponent
