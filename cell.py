from line import Line
from point import Point


class Cell:
    # Constructor initializes a cell with coordinates and windows reference
    def __init__(self, x1, y1, x2, y2, win=None):
        # Wall states - all walls exist by default
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

        # Store coordinates of cell boundaries
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        # Store the reference to window
        self._win = win

        # Visited attribute to check visited cells
        self.visited = False

    # Draw method to render the cell with its wall
    def draw(self):
        if self._win is None:
            return 
        
        wall_color = "black"
        bg_color = "white"
        
        # Draw left wall
        left_wall_color = wall_color if self.has_left_wall else bg_color
        line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
        self._win.draw_line(line, left_wall_color)
        
        # Draw right wall
        right_wall_color = wall_color if self.has_right_wall else bg_color
        line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
        self._win.draw_line(line, right_wall_color)
        
        # Draw top wall
        top_wall_color = wall_color if self.has_top_wall else bg_color
        line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
        self._win.draw_line(line, top_wall_color)
        
        # Draw bottom wall
        bottom_wall_color = wall_color if self.has_bottom_wall else bg_color
        line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
        self._win.draw_line(line, bottom_wall_color)


    def draw_move(self, to_cell, undo=False):
        # Calculate center point of current cell
        current_cell_center_x = (self._x1 + self._x2) / 2 
        current_cell_center_y = (self._y1 + self._y2) / 2 

        # Calculate center point of destination cell 
        to_cell_center_x = (to_cell._x1 + to_cell._x2) / 2
        to_cell_center_y = (to_cell._y1 + to_cell._y2) / 2 

        # Create points for the line 
        from_point = Point(current_cell_center_x, current_cell_center_y)
        to_point = Point(to_cell_center_x, to_cell_center_y)

        # Create line between the centers 
        line = Line(from_point, to_point)

        # Choose color based on undo tag 
        color = "gray" if undo else "red"

        # Draw the line using the widnow's draw_line method 
        self._win.draw_line(line, color)