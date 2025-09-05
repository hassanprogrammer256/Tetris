import pygame,sys
from Grid import Grid
from Game import Game
from Blocks import *
from constants import WINDOW_HEIGHT,WINDOW_WIDTH,FPS

pygame.init()
pygame.display.set_caption('Tetris Game by> Hassan')
pygame.display.set_icon(pygame.image.load('./images/icon.png'))
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
clock = pygame.time.Clock()

oGame = Game(window)

Running = True
while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running  = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                oGame.move_left()
            if event.key == pygame.K_RIGHT:
                oGame.move_right()
            if event.key == pygame.K_DOWN:
                oGame.move_down()
            
    oGame.draw()
    pygame.display.update()
    clock.tick(FPS)
    
pygame.quit()
sys.exit()
    



