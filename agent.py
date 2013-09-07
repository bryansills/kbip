from random import choice

class Agent:
    def __init__(self, side):
        self.side = side

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
        result = []

        if board[2][2].state == self.side and board[0][0].state == '-':
            result.append((0,0))

        if board[0][2].state == self.side and board[2][0].state == '-':
            result.append((2,0))

        if board[2][0].state == self.side and board[0][2].state == '-':
            result.append((0,2))

        if board[0][0].state == self.side and board[2][2].state == '-':
            result.append((2,2))

        return result


    def cornerSpots(self, board):
        result = []

        if board[0][0].state == '-':
            result.append((0,0))

        if board[2][0].state == '-':
            result.append((2,0))

        if board[0][2].state == '-':
            result.append((0,2))

        if board[2][2].state == '-':
            result.append((2,2))

        return result
