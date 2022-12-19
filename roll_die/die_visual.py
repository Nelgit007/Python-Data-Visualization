from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Create a die with six(D6) sides by instantiation
die = Die()

# Make die rolls, and store results in list
results = []
#make die roll five thousand times
for roll_num in range(5000):
	result = die.roll_die()
	results.append(result)

# Analyze the results
# NB: for each die we can have a max value of 8 and a minimum of 1
frequencies = []
for value in range(1, die.num_sides+1):
	frequency = results.count(value)
	frequencies.append(frequency)

# Visualizing the results from die rolls
x_values = list(range(1, die.num_sides+1))
# Define a data object
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Results'}
y_axis_config = {'title': 'Frequency of Result'}
# Adding a title
my_layout = Layout(title='Result of rolling a six sided die(D6), 1000 times', 
					xaxis=x_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')

print(frequencies)

