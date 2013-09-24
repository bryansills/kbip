from domknow import *
from agent import Agent
from random import choice

class Dumb(Agent):
    def makeMove(self, board):
        options = winningSpots(board, self.side)
        if len(options) != 0:
            return (choice(options), "This spot wins the game.")

        options = openSpots(board, self.side)
        if len(options) != 0:
            return (choice(options), "This spot is available.")
