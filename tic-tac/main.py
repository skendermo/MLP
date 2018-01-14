"""Module implements Machine Learning algorithm for a Tic-Tac-Toe game."""
import sys
import random

from time import sleep

# 3rd party libraries
import numpy


class Game(object):
    """docstring for Game."""

    def __init__(self, **arg):
        super(Game, self).__init__()
        self.arg = arg

    def get_random_matrix(self):
        """Output[list]: ([0, 1, 0], [1, 0, 1], [0, 1, 1])."""
        return numpy.random.randint(2, size=(3,3))

    def print_matrix(self, matrix):
        """Input[iterable]: matrix = ([0, 1, 0], [1, 0, 1], [0, 1, 1])
        Output: Tic-Tac-Toe board"""
        for row in matrix:
            val = lambda x: 'x' if x else 'o'
            cols = [val(col) for col in row]

            line = '[%s, %s, %s]' % (cols[0], cols[1], cols[2])

            print(line)

    def check_if_winning_ticket(self):
        """TODO
        Checks if the 3x3 matrix has a winning row, column or diagonal."""
        pass

    def rules(self):
        """TODO
        Implement the rules of the game."""
        pass


def main():
    """Run the program in the terminal."""

    user_input = input("How many games to print?: ")
    rounds = int(user_input) # TODO: Check if input is a number

    game = Game()

    for itr in range(0, rounds):
        matrix = game.get_random_matrix()
        print('Game %d: ------------------' % (itr + 1))
        game.print_matrix(matrix)
        sleep(1)


if __name__ == '__main__':
   main()
