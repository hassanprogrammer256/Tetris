NUM_COLS = 10
NUM_ROWS = 20
CELL_SIZE = 30

WINDOW_WIDTH = 300
WINDOW_HEIGHT = 600
FPS = 20

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (238, 255, 0)
GREEN = (0, 255, 0)
GREY = (31, 30, 30)
ORANGE = (255, 115, 0)
PURPLE = (116, 12, 129)
CYAN = (0, 255, 255)

class Colors:
  @staticmethod
  def get_colors():
      return [GREY,BLUE,YELLOW,GREEN,RED,ORANGE,PURPLE,CYAN]
  
class Position:
    def __init__(self,x,y):
       self.x = x
       self.y = y
