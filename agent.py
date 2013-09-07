from random import choice

class Agent:
    def __init__(self, side):
        self.side = side

    def makeMove(self, board):
        options = self.openSpots(board)

        return choice(options)

    def openSpots(self, board):
        result = []
        for row in range(3):
            for col in range(3):
                if board[row][col].state == '-':
                    result.append((row, col))

        return result

    def winningSpots(self, board):
        return []

    def blockLosingSpots(self, board):
        return []

    def oppositeCornerSpots(self, board):
        return []

    def cornerSpots(self, board):
        return []
