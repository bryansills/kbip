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
        result = []

        # check horizontal x
        for row in range(3):
            count = 0
            for ind in range(3):
                if board[row][ind].state == self.side:
                    count = count + 1

            if count >= 2:
                for ind in range(3):
                    if board[row][ind].state == '-':
                        result.append((row, ind))

        # check vertical x
        for col in range(3):
            count = 0
            for ind in range(3):
                if board[ind][col].state == self.side:
                    count = count + 1

            if count >= 2:
                for ind in range(3):
                    if board[ind][col].state == '-':
                        result.append((ind, col))

        # check diagonal x
        count = 0
        for ind in range(3):
            if board[ind][ind].state == self.side:
                count = count + 1

        if count >= 2:
            for ind in range(3):
                if board[ind][ind].state == '-':
                    result.append((ind, ind))


        count = 0
        for ind in range(3):
            if board[2 - ind][ind].state == self.side:
                count = count + 1

        if count >= 2:
            for ind in range(3):
                if board[2 - ind][ind].state == '-':
                    result.append((2 - ind, ind))

        return result


    def blockLosingSpots(self, board):
        result = []

        # check horizontal x
        for row in range(3):
            count = 0
            for ind in range(3):
                if board[row][ind].state != self.side and board[row][ind].state != '-':
                    count = count + 1

            if count >= 2:
                for ind in range(3):
                    if board[row][ind].state == '-':
                        result.append((row, ind))

        # check vertical x
        for col in range(3):
            count = 0
            for ind in range(3):
                if board[ind][col].state != self.side and board[ind][col].state != '-':
                    count = count + 1

            if count >= 2:
                for ind in range(3):
                    if board[ind][col].state == '-':
                        result.append((ind, col))

        # check diagonal x
        count = 0
        for ind in range(3):
            if board[ind][ind].state != self.side and board[ind][ind].state != '-':
                count = count + 1

        if count >= 2:
            for ind in range(3):
                if board[ind][ind].state == '-':
                    result.append((ind, ind))


        count = 0
        for ind in range(3):
            if board[2 - ind][ind].state != self.side and board[2 - ind][ind].state != '-':
                count = count + 1

        if count >= 2:
            for ind in range(3):
                if board[2 - ind][ind].state == '-':
                    result.append((2 - ind, ind))

        return result

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
