class Player:

    VALID_MOVES = ['rock', 'paper', 'scissors']

    def __init__(self):
        self.score = 0
        self.last_move_player = ''
        self.last_move_opponent = ''

    def move(self) -> str:
        """
        The Player class is the parent class for
        all of the Players in this game

        Default player always throws 'rock'
        Subclass Player to make a more complex game
        """
        return Player.VALID_MOVES[0]

    def learn(self, my_move, their_move):
        self.last_move_player = my_move
        self.last_move_opponent = their_move
