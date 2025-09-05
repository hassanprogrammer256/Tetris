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
        tiles = self.get_tile_positions()
        for tile in tiles:
            tile_rect = pygame.Rect(tile.x * self.cell_size + 1, tile.y * self.cell_size + 1,self.cell_size - 1, self.cell_size - 1)
            pygame.draw.rect(self.window,self.colors[self.id],tile_rect)
            
    def move(self,x,y) -> None:
        self.rows_offset += x
        self.columns_offset += y
        
    def get_tile_positions(self) -> list:
        tiles = self.cells[self.rotation_state]
        moved_tiles = []
        for pos in tiles:
            position = Position(pos.x + self.rows_offset, pos.y + self.columns_offset)
            moved_tiles.append(position)
        return moved_tiles
                      
class L_Block(Block):
    def __init__(self,window):
        super().__init__(window=window,id=1)
        self.cells = {
            0: [Position(0,2),Position(1,0),Position(1,1),Position(1,2),],
            1: [Position(0,1),Position(1,1),Position(2,1),Position(2,2),],
            2: [Position(1,0),Position(1,1),Position(1,2),Position(2,0),],
            3: [Position(0,0),Position(0,1),Position(1,1),Position(2,1),]}
        self.move(4,0)

class J_Block(Block):
    def __init__(self,window):
        super().__init__(window=window,id=2)
        self.cells = {
           0: [Position(0,0), Position(1,0), Position(1,1), Position(1,2)],
            1: [Position(0,1), Position(0,2), Position(1,1), Position(2,1)],
            2: [Position(1,0), Position(1,1), Position(1,2), Position(2,2)],
            3: [Position(0,1), Position(1,1), Position(2,0), Position(2,1)]}
        self.move(4,0)
        
class I_Block(Block):
    def __init__(self,window):
        super().__init__(window=window,id=3)
        self.cells = {
            0: [Position(1,0), Position(1,1), Position(1,2), Position(1,3)],
            1: [Position(0,2), Position(1,2), Position(2,2), Position(3,2)],
            2: [Position(2,0), Position(2,1), Position(2,2), Position(2,3)],
            3: [Position(0,1), Position(1,1), Position(2,1), Position(3,1)]}
        self.move(4,0)
        
class O_Block(Block):
    def __init__(self,window):
        super().__init__(window=window,id=4)
        self.cells = {
            0: [Position(0,0), Position(0,1), Position(1,0), Position(1,1)],
            1: [Position(0,0), Position(0,1), Position(1,0), Position(1,1)],
            2: [Position(0,0), Position(0,1), Position(1,0), Position(1,1)],
            3: [Position(0,0), Position(0,1), Position(1,0), Position(1,1)]}
        self.move(4,0)
        
class S_Block(Block):
    def __init__(self,window):
        super().__init__(window=window,id=5)
        self.cells = {
            0: [Position(0,1), Position(0,2), Position(1,0), Position(1,1)],
            1: [Position(0,1), Position(1,1), Position(1,2), Position(2,2)],
            2: [Position(1,1), Position(1,2), Position(2,0), Position(2,1)],
            3: [Position(0,0), Position(1,0), Position(1,1), Position(2,1)]}
        self.move(4,0)
        
class T_Block(Block):
    def __init__(self,window):
        super().__init__(window=window,id=6)
        self.cells = {
            0: [Position(0,1), Position(1,0), Position(1,1), Position(1,2)],
            1: [Position(0,1), Position(1,1), Position(1,2), Position(2,1)],
            2: [Position(1,0), Position(1,1), Position(1,2), Position(2,1)],
            3: [Position(0,1), Position(1,0), Position(1,1), Position(2,1)]}
        self.move(4,0)
        
class Z_Block(Block):
    def __init__(self,window):
        super().__init__(window=window,id=7)
        self.cells = {
            0: [Position(0,0), Position(0,1), Position(1,1), Position(1,2)],
            1: [Position(0,2), Position(1,1), Position(1,2), Position(2,1)],
            2: [Position(1,0), Position(1,1), Position(2,1), Position(2,2)],
            3: [Position(0,1), Position(1,0), Position(1,1), Position(2,0)]}
        self.move(4,0)