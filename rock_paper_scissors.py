#!/usr/bin/env python3

# This program plays a game of Rock, Paper, Scissors between
# two Players and reports both Player's scores each round.

from player import Player
from human_player import HumanPlayer
from random_player import RandomPlayer
from reflect_player import ReflectPlayer
from game import Game


if __name__ == '__main__':
    game = Game(HumanPlayer(), ReflectPlayer())
    game.play_game()
