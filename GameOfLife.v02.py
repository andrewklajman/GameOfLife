##2/1/2017
import time
import pygame

LIVE = '0'
DEAD = '-'

PIXWIDTH = 800
PIXHEIGHT = 600
WHITE = (255,255,255)
BLACK = (0,0,0)

initBoard = 'glidergun.txt'
board = [[char for char in line.rstrip('\n')] for line in open(initBoard,'r')]
BOARDWIDTH = len(board[0])
BOARDHEIGHT = len(board)

pygame.init()
gameDisplay = pygame.display.set_mode((PIXWIDTH, PIXHEIGHT))
pygame.display.set_caption('Andrews Game of Life')
clock = pygame.time.Clock()

def nextState(CurR, CurC):
    aliveNeighbours = sum([board[a][b]==LIVE for a in range(CurR - 1, CurR + 2) for b in range(CurC - 1, CurC + 2) if not(a == CurR and b == CurC) and 0 <= a < BOARDHEIGHT and 0 <= b < BOARDWIDTH])
    if (board[CurR][CurC] == LIVE and (aliveNeighbours == 2 or aliveNeighbours == 3)) or (board[CurR][CurC] == DEAD and aliveNeighbours == 3):
        return LIVE
    return DEAD

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    gameDisplay.fill(WHITE)
    [pygame.draw.rect(gameDisplay, BLACK, [c*11, r*11, 10,10]) for c in range(BOARDWIDTH) for r in range(BOARDHEIGHT) if board[r][c] == LIVE]
    board = [[nextState(r,c) for c in range(len(board[r]))] for r in range(len(board))]
    pygame.display.update()
    clock.tick(60)

