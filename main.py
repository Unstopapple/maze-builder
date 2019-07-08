from maze import *
from graphics import *

# set up the window size and grid size.
window_size = 400
cell_scale = 40
cell_size = window_size / cell_scale
# start drawing the window.
maze_win = GraphWin('Maze maker', window_size, window_size)

grid = []
y, x = 0, 0

while y*cell_size < window_size:
	while x*cell_size < window_size:
		grid.append((x, y))
		x += cell_size
	y += cell_size

# create the stack so we can populate the window with cells.
maze = Maze(maze_win)
maze_win.getMouse()
