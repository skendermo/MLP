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
        # Output: ([0, 1, 0], [1, 0, 1], [0, 1, 1])
        return numpy.random.randint(2, size=(3,3))


    def print_matrix(self, matrix):
        # Input[iterable]: matrix = ([0, 1, 0], [1, 0, 1], [0, 1, 1])
        # Output: Tic-Tac-Toe board
        for row in matrix:
            val = lambda x: 'x' if x else 'o'
            cols = [val(col) for col in row]

            line = '[%s, %s, %s]' % (cols[0], cols[1], cols[2])

            print(line)


def main():
    """Run the program in the terminal."""

    # To accept input from user
    # var = input("Please enter something: ")
    # print("You entered " + str(var))

    game = Game()

    for itr in range(0, 10):
        matrix = game.get_random_matrix()
        print('Game %d: ------------------' % (itr + 1))
        game.print_matrix(matrix)
        sleep(1)



if __name__ == '__main__':
   main()
