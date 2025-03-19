from window import *
from maze import *

def main():
    window = Window(1300, 1300)
    x_padding = 10
    y_padding = 10
    cells = 40
    cell_width = 32
    maze = Maze(x_padding, y_padding, cells, cells, cell_width, cell_width, window,)
    print(f"seed:{maze._seed}")
    window.wait_for_close()

main()