import pygame
from constants import CELL_SIZE,Colors,Position


class Block:
    def __init__(self,id:int,window:pygame.surface):
        self.id = id
        self.window = window
        self.cells = {}
        self.rotation_state = 0
        self.rows_offset = 0
        self.columns_offset = 0
        self.colors = Colors.get_colors()
        self.cell_size = CELL_SIZE
        
    def draw(self) -> None:
        tiles = self.cells[self.rotation_state]
        for tile in tiles:
            tile_rect = pygame.Rect(tile.x * self.cell_size + 1, tile.y * self.cell_size + 1,self.cell_size - 1, self.cell_size - 1)
            pygame.draw.rect(self.window,self.colors[self.id],tile_rect)
            
    
            
            
class L_Block(Block):
    def __init__(self,window):
        super().__init__(window=window,id=1)
        self.cells = {
            0: [Position(0,2),Position(1,0),Position(1,1),Position(1,2),],
            1: [Position(0,1),Position(1,1),Position(2,1),Position(2,2),],
            2: [Position(1,0),Position(1,1),Position(1,2),Position(2,0),],
            3: [Position(0,0),Position(0,1),Position(1,1),Position(2,1),],
        }
            