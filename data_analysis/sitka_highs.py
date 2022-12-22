import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	print(header_row)

	# Get high temperature and dates from this file
	print('- Records of TMAX for July 2018.')
	dates, highs = [], []
	for row in reader:
		current_date = datetime.strptime(row[2], '%Y-%m-%d')
		high = int(row[5])
		dates.append(current_date)
		highs.append(high)

# Plot high Temperatures
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')

# Set Chart Title and Label Axis
ax.set_title("Daily High Temperatures for the year 2018", fontsize=24)
ax.set_xlabel("", fontsize=14)
# Dispaly dates diagonally, call the autoformat
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=14)
# Set size of thick labels
ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()

	#for index, column_header in enumerate(header_row):
		#print(index, column_header)