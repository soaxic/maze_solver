from window import *
from maze import *

def main():
    window = Window(1300, 1300)
    maze = Maze(10, 10, 20, 20, 64, 64, window)
    maze._break_entrance_and_exit()
    window.wait_for_close()

main()