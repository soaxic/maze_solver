import time, random
from cell import Cell

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, window=None, seed=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._window = window
        if seed is not None:
            random.seed(seed)
        self._seed = random.random()
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()
        self._solve()
    
    def _create_cells(self):
        self._cells = []
        for i in range(self.num_cols):
            column = []
            for j in range(self.num_rows):
                column.append(Cell(self._window))
            self._cells.append(column)
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)
        
    def _draw_cell(self, i, j):
        if self._window is None:
            return
        x1 = self.x1 + self.cell_size_x * i
        y1 = self.y1 + self.cell_size_y * j
        x2 = self.x1 + self.cell_size_x * i + self.cell_size_x
        y2 = self.y1 + self.cell_size_y * j + self.cell_size_y

        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        self._window.redraw()
        time.sleep(0.01)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[-1][-1].has_bot_wall = False
        self._draw_cell(len(self._cells)-1,len(self._cells[-1])-1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            try:
                if self._cells[i-1][j].visited is False and i-1 >= 0:
                    to_visit.append((i-1, j))
            except IndexError:
                pass
            try:
                if self._cells[i+1][j].visited is False:
                    to_visit.append((i+1, j))
            except IndexError:
                pass
            try:
                if self._cells[i][j-1].visited is False and j-1 >= 0:
                    to_visit.append((i, j-1))
            except IndexError:
                pass
            try:
                if self._cells[i][j+1].visited is False:
                    to_visit.append((i, j+1))
            except IndexError:
                pass
            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return
            direction = random.randrange(0, len(to_visit), 1)
            x = to_visit[direction][0]
            y = to_visit[direction][1]
            if x > i:
                self._cells[i][j].has_right_wall = False
                self._cells[x][y].has_left_wall = False
            if x < i:
                self._cells[i][j].has_left_wall = False
                self._cells[x][y].has_right_wall = False
            if y > j:
                self._cells[i][j].has_bot_wall = False
                self._cells[x][y].has_top_wall = False
            if y < j:
                self._cells[i][j].has_top_wall = False
                self._cells[x][y].has_bot_wall = False
            self._break_walls_r(x, y)

    def _reset_cells_visited(self):
        for x in range(self.num_cols):
            for y in range(self.num_rows):
                self._cells[x][y].visited = False

    def _solve(self):
        return self._solve_r(0, 0)
    
    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        if i == self.num_cols - 1 and j == self.num_rows - 1:
            return True
        try:
            if self._cells[i-1][j].visited is False and i-1 >= 0 and not self._cells[i][j].has_left_wall:
                self._cells[i][j].draw_move(self._cells[i-1][j])
                if self._solve_r(i-1, j):
                    return True
                self._cells[i][j].draw_move(self._cells[i-1][j], True)
        except IndexError:
            pass
        try:
            if self._cells[i+1][j].visited is False and not self._cells[i][j].has_right_wall:
                self._cells[i][j].draw_move(self._cells[i+1][j])
                if self._solve_r(i+1, j):
                    return True
                self._cells[i][j].draw_move(self._cells[i+1][j], True)
        except IndexError:
            pass
        try:
            if self._cells[i][j-1].visited is False and j-1 >= 0 and not self._cells[i][j].has_top_wall:
                self._cells[i][j].draw_move(self._cells[i][j-1])
                if self._solve_r(i, j-1):
                    return True
                self._cells[i][j].draw_move(self._cells[i][j-1], True)
        except IndexError:
            pass
        try:
            if self._cells[i][j+1].visited is False and not self._cells[i][j].has_bot_wall:
                self._cells[i][j].draw_move(self._cells[i][j+1])
                if self._solve_r(i, j+1):
                    return True
                self._cells[i][j].draw_move(self._cells[i][j+1], True)
        except IndexError:
            pass
        return False