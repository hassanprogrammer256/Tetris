import pygame,random
from constants import Position,Colors,NUM_COLS,NUM_ROWS
from Grid import Grid
from Blocks import *

class Game:
    def __init__(self,window):
        self.window = window
        self.grid = Grid(self.window)
        self.blocks = [I_Block(self.window),L_Block(self.window),J_Block(self.window),O_Block(self.window),S_Block(self.window),Z_Block(self.window),T_Block(self.window)]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        
        
    def get_random_block(self) -> Block:
        if len(self.blocks) > 0:
            block = random.choice(self.blocks)
            self.blocks.remove(block)
            return block
        else:
            self.blocks = [I_Block(self.window),L_Block(self.window),J_Block(self.window),O_Block(self.window),S_Block(self.window),Z_Block(self.window),T_Block(self.window)]

    def is_inbounds(self,x,y) -> bool:
        if (x > 0 and x < NUM_ROWS and y > 0 and y < NUM_COLS):
            return True
        return False
    
    def blocks_inside(self) -> bool:
        tiles = self.current_block.get_tile_positions()
        for cell in tiles:
            if self.is_inbounds(cell.x, cell.y) == True:
                return True
        return False
        
    def move_left(self) -> None:
        self.current_block.move(-1,0) 
        if self.blocks_inside() == False:
            self.current_block.move(1,0)
        
    def move_right(self) -> None:
        self.current_block.move(1,0) 
        if self.blocks_inside() == False:
            self.current_block.move(-1,0)
        
    def move_down(self) -> None:
        self.current_block.move(0,1)
    
    def draw(self):
        self.grid.draw()
        self.current_block.draw()
        