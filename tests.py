import unittest
from maze import Maze
from cell import Cell

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)

    def test_maze_create_cells_small(self):
        num_cols = 2
        num_rows = 2
        m2 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m2._cells), num_cols)
        self.assertEqual(len(m2._cells[0]), num_rows)

    def test_break_entrance_and_exit(self):
        maze = Maze(x1=0, y1=0, num_rows=5, num_cols=5, cell_size_x=20, cell_size_y=20, win=None)
        maze._break_entrance_and_exit()

        # Verifica que la pared de entrada ha sido eliminada
        entrance_cell = maze._cells[0][0]
        assert entrance_cell.has_top_wall == False  # O has_left_wall

        # Verifica que la pared de salida ha sido eliminada
        exit_cell = maze._cells[maze._num_cols - 1][maze._num_rows - 1]
        assert exit_cell.has_bottom_wall == False  # O has_right_wall

    def test_reset__cells_visited(self):
        maze = Maze(x1=0, y1=0, num_rows=5, num_cols=5, cell_size_x=20, cell_size_y=20, win=None, seed=None)

        maze._break_entrance_and_exit()
        maze._break_walls_r(0,0)
        maze._reset_cells_visited()

        for col in range(maze._num_cols):
            for row in range(maze._num_rows):
                assert maze._cells[col][row].visited == False


        

if __name__ == "__main__":
    unittest.main()