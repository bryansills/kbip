from domknow import *
from smartknow import *
from agent import Agent
from random import choice

class Smart(Agent):
    def makeMove(self, board):
        return useStrategicKnowledge(board, self.side)
