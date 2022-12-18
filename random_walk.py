from random import choice

class RandomWalk:
	"""A class to generate random walk"""

	def __init__(self, num_points=500):
		"""Initializes the attributes of a walk"""
		self.num_points = num_points

		# Set all walks to start at (0, 0)
		self.x_values = [0]
		self.y_values = [0]

	def fill_walk(self):
		"""Calculates all points in the walk"""
		# Keeps taking steps until walk reaches desired length
		while len(self.x_values) < self.num_points:

			# Decide which direction to go and how far by calling the method get_step()
			x_step = self.get_step()
			y_step = self.get_step()

			#Calculate the new positions by adding step taken to x or y values
			x = self.x_values[-1] + x_step
			y = self.y_values[-1] + y_step

			#Append the new values to x and y
			self.x_values.append(x)
			self.y_values.append(y)

			#Reject moves going nowhere
			if x_step == 0 and y_step == 0:
				continue

	def get_step(self):
		"""Decides which directon to go and how far to go in the chosen direction"""
		directiion = choice([1, -1])
		distance = choice([0, 1, 2, 3, 4, 5, 6, 7])
		return directiion * distance



			
