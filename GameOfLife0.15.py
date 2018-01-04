import time
import os

LIVE = '0'
DEAD = '-'

BOARDHEIGHT = 100
BOARDWIDTH = 100

board = []

def initBoard(filename):
    return [[char for char in line.rstrip('\n')] for line in open(filename,'r')]
def printBoard(thisBoard):
    print('\n' * 50 + '\n'.join([''.join([c for c in line]) for line in thisBoard]))

def nextState(status,aliveNeighbours):
    if (status == LIVE and (aliveNeighbours == 2 or aliveNeighbours == 3)) or (status == DEAD and aliveNeighbours == 3):
        return LIVE
    else:
        return DEAD
print([a for a in range(3)]



def countNeighbours(CurR, CurC):
    aliveNeighbours = 0
    for r in range(CurR - 1, CurR + 2):
        for c in range(CurC - 1, CurC + 2):
            if not(r == CurR and c == CurC) and (0 <= r <= (BOARDHEIGHT-1)) and (0 <= c <= (BOARDWIDTH-1)) and board[r][c] == LIVE:
                aliveNeighbours += 1
    return aliveNeighbours

    
def main():
    global board,BOARDWIDTH,BOARDHEIGHT
    board = initBoard('glider.txt')
    BOARDWIDTH = len(board[0])
    BOARDHEIGHT = len(board)
    while True:
        printBoard(board)
        nextBoard = [[DEAD for i in range(BOARDWIDTH)] for j in range(BOARDHEIGHT)]
        for r in range(len(board)):
            for c in range(len(board[r])):
                nextBoard[r][c] = str(nextState(board[r][c], countNeighbours(r,c)))
        board = nextBoard
        time.sleep(.1)


main()

board = initBoard('boardFile.txt')
while True:
    printBoard(board)
    nextBoard = [[DEAD for i in range(BOARDWIDTH)] for j in range(BOARDHEIGHT)]
    for r in range(len(board)):
        for c in range(len(board[r])):
            nextBoard[r][c] = str(nextState(board[r][c], countNeighbours(r,c)))
    board = nextBoard
    time.sleep(1)
##
##printBoard(board)
##nextBoard = [[DEAD for i in range(BOARDWIDTH)] for j in range(BOARDHEIGHT)]
##for r in range(len(board)):
##    for c in range(len(board[r])):
##        nextBoard[r][c] = str(nextState(board[r][c], countNeighbours(r,c)))
##board = nextBoard
##
##printBoard(board)
##nextBoard = [[DEAD for i in range(BOARDWIDTH)] for j in range(BOARDHEIGHT)]
##for r in range(len(board)):
##    for c in range(len(board[r])):
##        nextBoard[r][c] = str(nextState(board[r][c], countNeighbours(r,c)))
##board = nextBoard


