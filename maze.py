
class Maze:
	def __init__(self, win):
		self.window = win
		self.cells = []
		self.current = []
		self.next = []
		self._wall = {"top": True, "bottom": True, "left": True, "right": True}

	def _toggle_wall(self, direction=''):
		if self._wall[direction]:
			self._wall[direction] = False
		else:
			self._wall[direction] = True

	def make_cell(self):
		pass

	def _draw_cell(self, x, y, size):
		pass
