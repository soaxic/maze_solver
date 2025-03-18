from graphics import Point, Line
from window import *

class Cell():
    def __init__(self, window=None):
        self.has_left_wall, self.has_right_wall, self.has_top_wall, self.has_bot_wall = True, True, True, True
        self._x1, self._x2, self._y1, self._y2 = None, None, None, None
        self._window = window

    def draw(self, x1, y1, x2, y2, breakwall=False):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if not breakwall:
            if self.has_left_wall:
                self._window.draw_line(Line(Point(x1, y1), Point(x1, y2)))
            if self.has_right_wall:
                self._window.draw_line(Line(Point(x2, y1), Point(x2, y2)))
            if self.has_top_wall:
                self._window.draw_line(Line(Point(x1, y1), Point(x2, y1)))
            if self.has_bot_wall:
                self._window.draw_line(Line(Point(x1, y2), Point(x2, y2)))
        else:
            if not self.has_left_wall:
                self._window.draw_line(Line(Point(x1, y1), Point(x1, y2)), "black")
            if not self.has_right_wall:
                self._window.draw_line(Line(Point(x2, y1), Point(x2, y2)), "black")
            if not self.has_top_wall:
                self._window.draw_line(Line(Point(x1, y1), Point(x2, y1)), "black")
            if not self.has_bot_wall:
                self._window.draw_line(Line(Point(x1, y2), Point(x2, y2)), "black")


    def draw_move(self, to_cell, undo=False):
        line = Line(self.get_center_point(), to_cell.get_center_point())
        if undo:
            self._window.draw_line(line, "gray")
        else:
            self._window.draw_line(line, "red")

    def get_center_point(self):
        center_x = int((self._x1 + self._x2) // 2)
        center_y = int((self._y1 + self._y2) // 2)
        return Point(center_x, center_y)
    
    def __repr__(self):
        return f"Cell@{self._window}({self._x1}, {self._y1}, {self._x2}, {self._y2})"