import pygame
from constants import *

class Grid:
    def __init__(self,window:pygame.surface):
        self.rows= NUM_ROWS
        self.cols= NUM_COLS
        self.cell_size = CELL_SIZE
        self.grid=  [[0 for i in range(self.cols)] for j in range(self.rows)]
        self.colors = Colors.get_colors()
        self.window = window
        
        
    def draw(self) -> None:
        for i in range(self.rows):
            for j in range(self.cols):
                cell_value = self.grid[i][j]
                cell_rect = pygame.Rect(j * self.cell_size +1,i * self.cell_size + 1,self.cell_size-1,self.cell_size-1)
                pygame.draw.rect(self.window,self.colors[cell_value],cell_rect)
        