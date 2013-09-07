from tile import *

class Game:    
    def __init__(self, agent1, agent2, board=[[Tile() for j in range(3)] for i in range(3)]):
        self.agent1 = agent1
        self.agent2 = agent2
        self.board = board

    def run(self):
        agentOneTurn = True

        while result == 'Nope' and len(openSpots()) != 0:
            if playerOneTurn:
                print('agentonemove')
                agentOneTurn = False
            else:
                print('agenttwomove')
                agentOneTurn = True

            result = checkForWin()

        if result == 'X':
            return 'X'
        else if result == 'O':
            return 'O'
        else:
            print('Something fucked up...')


    def openSpots(self):
        openSpots = []
        for row in range(3):
            for col in range(3):
                if self.board[row][col].state == '-':
                    openSpots.append((row, col))

        return openSpots

    def checkForWin(self):
        # check horizontal x
        for row in range(3):
            if 'X' == self.board[row][0].state == self.board[row][1].state == self.board[row][2].state:
                return 'X'
        # check vertical x
        for col in range(3):
            if 'X' == self.board[0][col].state == self.board[1][col].state == self.board[2][col].state:
                return 'X'
        # check diagonal x
        if 'X' == self.board[0][0].state == self.board[1][1].state == self.board[2][2].state:
            return 'X'
        if 'X' == self.board[2][0].state == self.board[1][1].state == self.board[0][2].state:
            return 'X'

        # check horizontal o
        for row in range(3):
            if 'O' == self.board[row][0].state == self.board[row][1].state == self.board[row][2].state:
                return 'O'
        # check vertical o
        for col in range(3):
            if 'O' == self.board[0][col].state == self.board[1][col].state == self.board[2][col].state:
                return 'O'
        # check diagonal o
        if 'O' == self.board[0][0].state == self.board[1][1].state == self.board[2][2].state:
            return 'O'
        if 'O' == self.board[2][0].state == self.board[1][1].state == self.board[0][2].state:
            return 'O'

        return 'Nope'

    def printBoard(self):
        print(self.board[0][0].state + '|' + self.board[0][1].state + '|' + self.board[0][2].state)
        print('-----')
        print(self.board[1][0].state + '|' + self.board[1][1].state + '|' + self.board[1][2].state)
        print('-----')
        print(self.board[2][0].state + '|' + self.board[2][1].state + '|' + self.board[2][2].state)

y = Tile('X')
brd = [[Tile('X'),Tile('-'),Tile('-')],[Tile('O'),Tile('X'),Tile('O')],[Tile('X'),Tile('-'),Tile('X')]]
x = Game('this', 'that', brd)

print(x.openSpots())

x.printBoard()