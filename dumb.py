from agent import Agent
from random import choice

class Dumb(Agent):
    def makeMove(self, board):
        options = self.winningSpots(board)
        if len(options) != 0:
            return choice(options)

        options = self.openSpots(board)
        if len(options) != 0:
            return choice(options)
