from graphics import *
from maze import *

# set up the window size and grid size.
window_size = 400
cell_scale = 40
cell_size = window_size / cell_scale
# start drawing the window.
maze_win = GraphWin('Maze maker', window_size, window_size)
# create the stack so we can populate the window with cells.
stack = Maze(maze_win)
maze_win.getMouse()

