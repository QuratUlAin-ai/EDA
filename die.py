from random import randrange

class Die:
	def __init__(self, num_sides=6):
		self.num_sides = num_sides

	def roll(self):
		return randrange(1, self.num_sides)