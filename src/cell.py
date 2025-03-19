import random
from graphics import Point, Line
from window import *

class Cell():
    def __init__(self, window=None):
        self.has_left_wall, self.has_right_wall, self.has_top_wall, self.has_bot_wall = True, True, True, True
        self._x1, self._x2, self._y1, self._y2 = None, None, None, None
        self._window = window
        self.visited = False

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_left_wall:
            self._window.draw_line(Line(Point(x1, y1), Point(x1, y2)))
        else:
            self._window.draw_line(Line(Point(x1, y1), Point(x1, y2)), "black")
        if self.has_right_wall:
            self._window.draw_line(Line(Point(x2, y1), Point(x2, y2)))
        else:
            self._window.draw_line(Line(Point(x2, y1), Point(x2, y2)), "black")
        if self.has_top_wall:
            self._window.draw_line(Line(Point(x1, y1), Point(x2, y1)))
        else:
            self._window.draw_line(Line(Point(x1, y1), Point(x2, y1)), "black")
        if self.has_bot_wall:
            self._window.draw_line(Line(Point(x1, y2), Point(x2, y2)))
        else:
            self._window.draw_line(Line(Point(x1, y2), Point(x2, y2)), "black")


    def draw_move(self, to_cell, undo=False):
        line = Line(self.get_center_point(), to_cell.get_center_point())
        if undo:
            r = hex(random.randint(1023,4095))[2:].zfill(3)
            g = hex(random.randint(1023,4095))[2:].zfill(3)
            b = hex(random.randint(1023,4095))[2:].zfill(3)
            rgb = "#" + str(r) + str(g) + str(b)
            self._window.draw_line(line, rgb)
        else:
            self._window.draw_line(line, "red")

    def get_center_point(self):
        center_x = int((self._x1 + self._x2) // 2)
        center_y = int((self._y1 + self._y2) // 2)
        return Point(center_x, center_y)
    
    def __repr__(self):
        return f"Cell@{self._window} ({self._x1}, {self._y1}, {self._x2}, {self._y2}) v={self.visited}\n"