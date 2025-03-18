from tkinter import Tk, BOTH, Canvas
from graphics import *
from cell import *

class Window():
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title("Maze Solver")
        self.canvas = Canvas(self.root, height=height, width=width, background="black",)
        self.canvas.pack()
        self.running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
        print("Closing...")

    def close(self):
        self.running = False

    def draw_line(self, line, fill_color="white"):
        line.draw(self.canvas, fill_color)

    def __repr__(self):
        return str(self.root.title())