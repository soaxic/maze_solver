from graphics import Point, Line
from window import Window

class Cell():
    def __init__(self, window):
        self.has_left_wall, self.has_right_wall, self.has_top_wall, self.has_bot_wall = True, True, True, True
        self._x1, self._x2, self._y1, self._y2 = None, None, None, None
        self._window = window

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_left_wall:
            self._window.draw_line(Line(Point(x1, y1), Point(x1, y2)))
        if self.has_right_wall:
            self._window.draw_line(Line(Point(x2, y1), Point(x2, y2)))
        if self.has_top_wall:
            self._window.draw_line(Line(Point(x1, y1), Point(x2, y1)))
        if self.has_bot_wall:
            self._window.draw_line(Line(Point(x1, y2), Point(x2, y2)))

    def draw_move(self, to_cell, undo=False):
        line = Line(self.get_center_point(), to_cell.get_center_point())
        if undo:
            self._window.draw_line(line, "gray")
        else:
            self._window.draw_line(line)

    def get_center_point(self):
        center_x = int((self._x1 + self._x2) // 2)
        center_y = int((self._y1 + self._y2) // 2)
        return Point(center_x, center_y)