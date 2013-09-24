from domknow import *
from agent import Agent
from random import choice

class Smart(Agent):
    def makeMove(self, board):
        options = winningSpots(board, self.side)
        if len(options) != 0:
            return (choice(options), "This spot wins the game.")

        options = blockLosingSpots(board, self.side)
        if len(options) != 0:
            return (choice(options), "This spot blocks the opponent.")

        options = oppositeCornerSpots(board, self.side)
        if len(options) != 0:
            return (choice(options), "This spot is opposite of a corner you already claimed.")

        options = cornerSpots(board, self.side)
        if len(options) != 0:
            return (choice(options), "This spot is a corner spot.")

        options = openSpots(board, self.side)
        if len(options) != 0:
            return (choice(options), "This spot is available.")
