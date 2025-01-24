import time, random
from cell import Cell

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
    # Initialize maze properties 
        self._x1 = x1 
        self._y1 = y1 
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

    #Check seed is not None
        if seed is not None:
            random.seed(seed)

    # Initialize empty cells matrix 
        self._cells = []

    # Create and draw the cells 
        self._create_cells()

        self._break_entrance_and_exit()
        self._break_walls_r(0,0)

    def _create_cells(self):
    #    Create a matrix of cells (list of lists)
        for i in range(self._num_cols):
            # Create a new column 
            col = []
            for j in range(self._num_rows):
                # Add cells to the column 
                col.append(None) # Placeholder for now
            self._cells.append(col)

        # Fill in each cell and draw it 
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)


    def _draw_cell(self, i, j):
        # Calculate the coordinates for this cell 
        x1 = self._x1 + (i * self._cell_size_x)
        y1 = self._y1 + (j * self._cell_size_y)
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y 

        # Create new cell with calculated coordinates 
        cell = Cell(x1, y1, x2, y2, self._win)

        # Store the cell in our matrix 
        self._cells[i][j] = cell 

        # Draw the cell 
        cell.draw()

        # Animate the drawing 
        self._animate()

    def _animate(self):
        if self._win is None:
            return 
        
        # Redraw the window 
        self._win.redraw()

        # Pause briefly to allow visualization 
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        entrance_cell = self._cells[0][0]
        entrance_cell.has_top_wall = False
        entrance_cell.draw()

        exit_cell = self._cells[self._num_cols - 1][self._num_rows - 1]
        exit_cell.has_bottom_wall = False
        exit_cell.draw()

    def _break_walls_r(self, col, row):
        current_cell = self._cells[col][row]
        current_cell.visited = True

        while True:
            neighbors = []

            # Top (row - 1)
            if row > 0 and not self._cells[col][row - 1].visited:
                neighbors.append(('U', col, row - 1))

            # Bottom (row + 1)
            if row < self._num_rows - 1 and not self._cells[col][row + 1].visited:
                neighbors.append(('D', col, row + 1))

            # Left (col - 1)
            if col > 0 and not self._cells[col - 1][row].visited:
                neighbors.append(('L', col - 1, row))
            
            # Right (col + 1)
            if col < self._num_cols - 1 and not self._cells[col + 1][row].visited:
                neighbors.append(('R', col + 1, row))
    
            if not neighbors:
                # There are no neighbors to visit
                current_cell.draw()
                return
            
            # Choose a random neighbor
            direction, next_i, next_j = random.choice(neighbors)
            next_cell = self._cells[next_i][next_j]

            # Break walls between current_cell and next_cell
            if direction == 'U':
                current_cell.has_top_wall = False
                next_cell.has_bottom_wall = False
            elif direction == 'D':
                current_cell.has_bottom_wall = False
                next_cell.has_top_wall = False
            elif direction == 'L':
                current_cell.has_left_wall = False
                next_cell.has_right_wall = False
            elif direction == 'R':
                current_cell.has_right_wall = False
                next_cell.has_left_wall = False

            # Recurse call
            self._break_walls_r(next_i,next_j)

    def _reset_cells_visited(self):
        for col in range(self._num_cols):
            for row in range(self._num_rows):
                self._cells[col][row].visited = False

    def _solve_r(self, col, row):
        self._animate()

        current_cell = self._cells[col][row]
        current_cell.visited = True

        # Check if it is the final cell 
        if col == self._num_cols - 1 and row == self._num_rows - 1:
            return True
        
        # Try with every direction 
        directions = []
        # Top
        if row > 0 and not current_cell.has_top_wall:
            directions.append((col, row-1, 'U'))
        # Bottom
        if row < self._num_rows - 1 and not current_cell.has_bottom_wall:
            directions.append((col, row+1, 'D'))
        # Left
        if col > 0 and not current_cell.has_left_wall:
            directions.append((col-1, row, 'L'))
        # Right
        if col < self._num_cols - 1 and not current_cell.has_right_wall:
            directions.append((col+1, row, 'R'))

        # Check all directions
        for next_col, next_row, _dir in directions:
            neighbor_cell = self._cells[next_col][next_row]
            if not neighbor_cell.visited:
                # Draw movement
                current_cell.draw_move(neighbor_cell, undo=False)

                # Recursive call
                if self._solve_r(next_col, next_row):
                    return True
                else:
                    # Backwards (undo move)
                    current_cell.draw_move(neighbor_cell, undo=True)

        # if any direction worked, return False
        return False
        
    def solve(self):
        self._reset_cells_visited()
        return self._solve_r(0,0)