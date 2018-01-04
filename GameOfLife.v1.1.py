##http://www.conwaylife.com
import time
import pygame

LIVE = 'O'
DEAD = '-'
##INITBOARD = 'pic142.txt'
##INITBOARD = 'BigSpaceship.txt'
INITBOARD = 'acorn.txt'
SQUARE = 1
WHITE= (255,255,255)
BLACK = (0,0,0)
chgXPan = 100
chgYPan = 100
mousePosCur = 0
mousePresCur = 0
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

board = [[char for char in line.rstrip('\n')] for line in open(INITBOARD,'r')]
watch_alive = {(r,c):LIVE for r in range(len(board)) for c in range(len(board[0])) if board[r][c] == LIVE}
watch = {(r,c):DEAD for key in watch_alive.keys() for r in range(key[0] - 1, key[0] + 2) for c in range(key[1] - 1, key[1] + 2) if key != (r,c) and (r,c) not in watch_alive}

pygame.init()
gameDisplay = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
clock = pygame.time.Clock()

def aliveNeighbour(CurR, CurC):
    return len([(r,c) for c in range(CurC - 1, CurC+2) for r in range(CurR - 1, CurR + 2) if not (r == CurR and c == CurC) and (r,c) in watch_alive])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    gameDisplay.fill(WHITE)
    [pygame.draw.rect(gameDisplay,BLACK,[key[1]*(SQUARE + (SQUARE > 5) * 1) + chgYPan, key[0]*SQUARE + (SQUARE > 5) * 1 + chgXPan, SQUARE, SQUARE]) for key in watch_alive.keys()]

    watch.update(watch_alive)

    watch_alive = {key:LIVE for key in watch.keys() if (watch[key] == LIVE and 2 <= aliveNeighbour(key[0],key[1]) <= 3) or (watch[key] == DEAD and aliveNeighbour(key[0],key[1]) == 3)}
    watch = {(r,c):DEAD for key in watch_alive.keys() for r in range(key[0] - 1, key[0] + 2) for c in range(key[1] - 1, key[1] + 2) if key != (r,c) and (r,c) not in watch_alive}

    mousePosPrev = mousePosCur
    mousePosCur = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0] == 1:
        chgXPan = mousePosCur[1] - mousePosPrev[1] + chgXPan
        chgYPan = mousePosCur[0] - mousePosPrev[0] + chgYPan

    icon_plus = pygame.Surface((21,21))
    pygame.draw.line(icon_plus,WHITE,(2,10),(18,10),2)
    pygame.draw.line(icon_plus,WHITE,(10,2),(10,18),2)
    gameDisplay.blit(icon_plus, (5,5))
    icon_minus = pygame.Surface((21,21))
    pygame.draw.line(icon_minus,WHITE,(2,10),(18,10),2)
    gameDisplay.blit(icon_minus, (5,30))
    mousePresPrev = mousePresCur
    mousePresCur = pygame.mouse.get_pressed()[0]

    if mousePresCur == 1 and 5 <= mousePosCur[0] <= 26  and mousePresPrev == 0:
        if 5 <= mousePosCur[1] <= 26:
            SQUARE += .5
        if 30 <= mousePosCur[1] <= 51:
            SQUARE -= .5

    pygame.display.update()
    clock.tick(1000)


    








            
