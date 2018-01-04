##2/1/2017
import time
import os

LIVE = '0'
DEAD = '-'

def printBoard(thisBoard):
    print('\n' * 50 + '\n'.join([''.join([c for c in line]) for line in thisBoard]))

def nextState(CurR, CurC):
    aliveNeighbours = sum([board[a][b]==LIVE for a in range(CurR - 1, CurR + 2) for b in range(CurC - 1, CurC + 2) if not(a == CurR and b == CurC) and 0 <= a < BOARDHEIGHT and 0 <= b < BOARDWIDTH])
    if (board[CurR][CurC] == LIVE and (aliveNeighbours == 2 or aliveNeighbours == 3)) or (board[CurR][CurC] == DEAD and aliveNeighbours == 3):
        return LIVE
    return DEAD

initBoard = 'glider.txt'
board = [[char for char in line.rstrip('\n')] for line in open(initBoard,'r')]
BOARDWIDTH = len(board[0])
BOARDHEIGHT = len(board)
while True:
    printBoard(board)
    board = [[nextState(r,c) for c in range(len(board[r]))] for r in range(len(board))]
    time.sleep(.1)
