#File Name: PracticeShapes.py

import pygame, sys
pygame.init()
screen=pygame.display.set_mode([800, 800])
screen.fill([0,0,0])
for i in range(8):
    for j in range(8):
        if i%2 == 0:
            if j%2 == 0:
                pygame.draw.rect(screen,[255,0,0], [i*100, j*100, 100, 100], 0)
            else:
                pygame.draw.rect(screen, [0, 0, 0], [i * 100, j * 100, 100, 100], 0)
                if j == 5 or j == 7:
                    pygame.draw.circle(screen, [100, 100, 100], [(i * 100) + 50, (j * 100) + 50], 40, 0)
                elif j == 1:
                    pygame.draw.circle(screen, [200, 0, 0], [(i * 100) + 50, (j * 100) + 50], 40, 0)
        elif i%2 == 1:
            if j%2 == 0:
                pygame.draw.rect(screen, [0, 0, 0], [i*100, j*100, 100, 100], 0)
                if j == 0 or j == 2:
                    pygame.draw.circle(screen, [200, 0, 0], [(i * 100) + 50, (j * 100) + 50], 40, 0)
                elif j == 6:
                    pygame.draw.circle(screen, [100, 100, 100], [(i * 100) + 50, (j * 100) + 50], 40, 0)
            else:
                pygame.draw.rect(screen, [255, 0, 0], [i * 100, j * 100, 100, 100], 0)




pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()