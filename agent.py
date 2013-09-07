from random import choice

class Agent:
    def __init__(self, side):
        self.side = side

    def makeMove(self, board):
        possibleMoves = self.openSpots(board)

        return choice(possibleMoves)

    def openSpots(self, board):
        result = []
        for row in range(3):
            for col in range(3):
                if board[row][col].state == '-':
                    result.append((row, col))

        return result