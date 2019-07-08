from graphics import *


class Maze:
	def __init__(self, win):
		self.window = win
		self.cells = []
		self.current = []
		self.next = []
		self.wall = {"top": True, "bottom": True, "left": True, "right": True}

	def _toggle_wall(self, direction=''):
		if self.wall[direction]:
			self.wall[direction] = False
		else:
			self.wall[direction] = True

	def make_cell(self):
		pass

	def _draw_cell(self, x, y, size):
		pass
