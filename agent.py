from random import choice

class Agent:
    def __init__(self, side):
        self.side = side

    def openSpots(self, board):
        result = []
        for row in range(3):
            for col in range(3):
                if board[row][col] == '-':
                    result.append((row, col))

        return result

    def winningSpots(self, board):
        result = []

        # check horizontal x
        for row in range(3):
            count = 0
            for ind in range(3):
                if board[row][ind] == self.side:
                    count = count + 1

            if count >= 2:
                for ind in range(3):
                    if board[row][ind] == '-':
                        result.append((row, ind))

        # check vertical x
        for col in range(3):
            count = 0
            for ind in range(3):
                if board[ind][col] == self.side:
                    count = count + 1

            if count >= 2:
                for ind in range(3):
                    if board[ind][col] == '-':
                        result.append((ind, col))

        # check diagonal x
        count = 0
        for ind in range(3):
            if board[ind][ind] == self.side:
                count = count + 1

        if count >= 2:
            for ind in range(3):
                if board[ind][ind] == '-':
                    result.append((ind, ind))


        count = 0
        for ind in range(3):
            if board[2 - ind][ind] == self.side:
                count = count + 1

        if count >= 2:
            for ind in range(3):
                if board[2 - ind][ind] == '-':
                    result.append((2 - ind, ind))

        return result


    def blockLosingSpots(self, board):
        result = []

        # check horizontal x
        for row in range(3):
            count = 0
            for ind in range(3):
                if board[row][ind] != self.side and board[row][ind] != '-':
                    count = count + 1

            if count >= 2:
                for ind in range(3):
                    if board[row][ind] == '-':
                        result.append((row, ind))

        # check vertical x
        for col in range(3):
            count = 0
            for ind in range(3):
                if board[ind][col] != self.side and board[ind][col] != '-':
                    count = count + 1

            if count >= 2:
                for ind in range(3):
                    if board[ind][col] == '-':
                        result.append((ind, col))

        # check diagonal x
        count = 0
        for ind in range(3):
            if board[ind][ind] != self.side and board[ind][ind] != '-':
                count = count + 1

        if count >= 2:
            for ind in range(3):
                if board[ind][ind] == '-':
                    result.append((ind, ind))


        count = 0
        for ind in range(3):
            if board[2 - ind][ind] != self.side and board[2 - ind][ind] != '-':
                count = count + 1

        if count >= 2:
            for ind in range(3):
                if board[2 - ind][ind] == '-':
                    result.append((2 - ind, ind))

        return result

    def oppositeCornerSpots(self, board):
        result = []

        if board[2][2] == self.side and board[0][0] == '-':
            result.append((0,0))

        if board[0][2] == self.side and board[2][0] == '-':
            result.append((2,0))

        if board[2][0] == self.side and board[0][2] == '-':
            result.append((0,2))

        if board[0][0] == self.side and board[2][2] == '-':
            result.append((2,2))

        return result


    def cornerSpots(self, board):
        result = []

        if board[0][0] == '-':
            result.append((0,0))

        if board[2][0] == '-':
            result.append((2,0))

        if board[0][2] == '-':
            result.append((0,2))

        if board[2][2] == '-':
            result.append((2,2))

        return result
