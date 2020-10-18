from player import Player
from random_player import RandomPlayer
from time import sleep


class Game:

    SCORE_TO_WIN = 3

    def __init__(self, p1, p2):
        self.current_round = 0
        self.p1 = p1
        self.p2 = p2
        self.winner_exists = False

    def clear_screen(self):
        print("\n" * 500)

    def play_game(self):
        self.clear_screen()
        print("Game start!\n")
        sleep(1.5)

        self.clear_screen()

        while not self.winner_exists:
            # add 1 for human readability
            print(f"Round {self.current_round + 1}:")
            self.play_round()
            self.current_round += 1

        print(f"GAME OVER - Total Rounds: {self.current_round}\n\n")
        self.print_winner()

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()

        # Scoring
        if self._beats(move1, move2):     # Player 1 wins round
            self.p1.score += 1
        elif self._beats(move2, move1):   # Player 2 wins round
            self.p2.score += 1

        self.clear_screen()
        print("=================================================")
        print(
            f"Player 1 Score: {self.p1.score}            Player 2 Score: "
            f"{self.p2.score}")
        print("=================================================\n\n")
        print(f"Player 1: {move1}     Player 2: {move2}\n\n")

        print("-------------------------------------------------\n\n\n\n\n\n")

        # Check for a winner
        if (self.p1.score == self.SCORE_TO_WIN) or\
           (self.p2.score == self.SCORE_TO_WIN):
            self.winner_exists = True

        # Learn move
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def print_winner(self):
        if self.p1.score > self.p2.score:
            print("Player 1 is the winner!\n")
        else:
            print("Player 2 is the winner!\n")

    def _beats(self, one, two):
        return ((one == 'rock' and two == 'scissors') or
                (one == 'scissors' and two == 'paper') or
                (one == 'paper' and two == 'rock'))
