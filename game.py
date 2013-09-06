from tile import *

class Game:    
    def __init__(self, agent1, agent2, board=[[Tile() for j in range(3)] for i in range(3)]):
        self.agent1 = agent1
        self.agent2 = agent2
        self.board = board

    def printBoard(self):
        print(self.board[0][0].state + '|' + self.board[0][1].state + '|' + self.board[0][2].state)
        print('-----')
        print(self.board[1][0].state + '|' + self.board[1][1].state + '|' + self.board[1][2].state)
        print('-----')
        print(self.board[2][0].state + '|' + self.board[2][1].state + '|' + self.board[2][2].state)

y = Tile('X')
brd = [[Tile('X'),Tile('X'),Tile('X')],[Tile('O'),Tile('O'),Tile('O')],[Tile('X'),Tile('X'),Tile('X')]]
x = Game('this', 'that', brd)


print(x.agent1 + ' blah ' + x.agent2)
x.printBoard()