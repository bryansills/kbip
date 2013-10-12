from dumbknow import *
from agent import Agent
from random import choice

class Dumb(Agent):
    def makeMove(self, board):
        return useStrategicKnowledge(board, self.side)
