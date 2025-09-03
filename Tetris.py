import pygame,sys
from Grid import Grid
from Blocks import *
from constants import WINDOW_HEIGHT,WINDOW_WIDTH,GREY,FPS
pygame.init()
pygame.display.set_caption('Tetris Game by> Hassan')
pygame.display.set_icon(pygame.image.load('./images/icon.png'))
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
clock = pygame.time.Clock()

oGrid = Grid(window)
lBlock = L_Block(window)

Running = True
while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running  = False
            
    oGrid.draw()
    lBlock.draw()
    pygame.display.update()
    clock.tick(FPS)
    
pygame.quit()
sys.exit()
    



