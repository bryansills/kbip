from smart import *
from dumb import *

class Game:    
    def __init__(self, agent1, agent2, board=None):
        self.agent1 = agent1
        self.agent2 = agent2
        if board is None:
            self.board = [["-" for j in range(3)] for i in range(3)]
        else:
            self.board = board

    def run(self):
        agentOneTurn = True
        result = 'Nope'

        while result == 'Nope' and len(self.openSpots()) != 0:
            if agentOneTurn:
                move, reason = self.agent1.makeMove(self.board)
                print("Agent 1 Reason: " + reason + ": " + str(move))
                self.board[move[0]][move[1]] = 'X'
                agentOneTurn = False
            else:
                move, reason = self.agent2.makeMove(self.board)
                print("Agent 2 Reason: " + reason + ": " + str(move))
                self.board[move[0]][move[1]] = 'O'
                agentOneTurn = True

            self.printBoard()
            result = self.checkForWin()

        if result == 'X':
            return 'X'
        elif result == 'O':
            return 'O'
        else:
            return 'Draw'


    def openSpots(self):
        result = []
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == '-':
                    result.append((row, col))

        return result

    def checkForWin(self):
        # check horizontal x
        for row in range(3):
            if 'X' == self.board[row][0] == self.board[row][1] == self.board[row][2]:
                return 'X'
        # check vertical x
        for col in range(3):
            if 'X' == self.board[0][col] == self.board[1][col] == self.board[2][col]:
                return 'X'
        # check diagonal x
        if 'X' == self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return 'X'
        if 'X' == self.board[2][0] == self.board[1][1] == self.board[0][2]:
            return 'X'

        # check horizontal o
        for row in range(3):
            if 'O' == self.board[row][0] == self.board[row][1] == self.board[row][2]:
                return 'O'
        # check vertical o
        for col in range(3):
            if 'O' == self.board[0][col] == self.board[1][col] == self.board[2][col]:
                return 'O'
        # check diagonal o
        if 'O' == self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return 'O'
        if 'O' == self.board[2][0] == self.board[1][1] == self.board[0][2]:
            return 'O'

        return 'Nope'

    def printBoard(self):
        print(self.board[0][0] + '|' + self.board[0][1] + '|' + self.board[0][2])
        print('-----')
        print(self.board[1][0] + '|' + self.board[1][1] + '|' + self.board[1][2])
        print('-----')
        print(self.board[2][0] + '|' + self.board[2][1] + '|' + self.board[2][2])
        print('')

countX2 = 0
countO2 = 0
countDraw2 = 0
for ind in range(1000):
    x = Game(Smart('X'), Dumb('O'))
    x.printBoard()
    result = x.run()

    if result == 'X':
        countX2 = countX2 + 1
    elif result == 'O':
        countO2 = countO2 + 1
    elif result == 'Draw':
        countDraw2 = countDraw2 + 1

countX3 = 0
countO3 = 0
countDraw3 = 0
for ind in range(1000):
    x = Game(Dumb('X'), Smart('O'))
    x.printBoard()
    result = x.run()

    if result == 'X':
        countX3 = countX3 + 1
    elif result == 'O':
        countO3 = countO3 + 1
    elif result == 'Draw':
        countDraw3 = countDraw3 + 1

print('Experiment 1: Smart X - ' + str(countX2) + ', Dumb O - ' + str(countO2) + ', Draw - ' + str(countDraw2))
print('Experiment 2: Dumb X - ' + str(countX3) + ', Smart O - ' + str(countO3) + ', Draw - ' + str(countDraw3))
