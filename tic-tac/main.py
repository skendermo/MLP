"""Module implements Machine Learning algorithm for a Tic-Tac-Toe game."""
import sys
from time import sleep


class Game(object):
    """docstring for Game."""

    def __init__(self, **arg):
        super(Game, self).__init__()
        self.arg = arg

    def print_matrix(self, matrix):
        # Input[tuple]: matrix = ([0, 1, 0], [1, 0, 1], [0, 1, 1])
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

    matrix = ([0, 1, 0], [1, 0, 1], [0, 1, 1])

    game = Game()
    game.print_matrix(matrix)


if __name__ == '__main__':
   main()
