from random import randint


class Die:
	"""A class to represent a single die"""

	def __init__(self, num_sides=6):
		"""Initialzes and assumes die to be six-sided"""
		self.num_sides = num_sides

	def roll_die(self):
		"""Returns a random value whenever die is rolled, any number between 1 & 6"""
		return randint(1, self.num_sides)
