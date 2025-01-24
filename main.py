from window import Window
from maze import Maze

def main():
    # Create new windowdow instance
    win = Window(800, 600)

    # Create maze with specific dimensions
    maze = Maze(50, 50, 10, 10, 40, 40, win)

    solved = maze.solve()
    if solved:
        print("Maze solved!")
    else:
        print("No solution found.")

    # wait for windowdow to close
    win.wait_for_close()


main()
