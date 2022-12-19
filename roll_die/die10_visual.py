from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Create a six(D6) and a ten(D10) sided die
die_1 = Die()
die_2 = Die()
die_3 = Die()

# Make die rolls, and store results in list
results = []
#make die roll five thousand times
for roll_num in range(50_000):
	result = die_1.roll_die() + die_2.roll_die() + die_3.roll_die()
	results.append(result)

# Analyze the results
# NB: For each die set, we can have a maximum value of 12 and a minimum value of 2
frequencies = []
max_results = die_1.num_sides + die_2.num_sides + die_3.num_sides
for value in range(3, max_results+1):
	frequency = results.count(value)
	frequencies.append(frequency)

# Visualizing the results from die rolls
x_values = list(range(3, max_results+1))
# Define a data object
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Results', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
# Adding a title
my_layout = Layout(title='Result for rolling three pair of dies with sides (D6), 50000 times', 
					xaxis=x_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d10.html')

print(frequencies)