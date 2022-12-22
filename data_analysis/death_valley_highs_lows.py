import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	print(header_row)

	# Get dates, high and low temperature from this file
	print('- Dates, TMIN and TMAX for July 2018.')
	dates, highs, lows = [], [], []
	for row in reader:
		current_date = datetime.strptime(row[2], '%Y-%m-%d')
		try:
			low = int(row[5])
			high = int(row[4])
		except ValueError:
			print(f"Missing data at {current_date}")
		else:
			dates.append(current_date)
			highs.append(high)
			lows.append(low)

# Plot for the high and low Temperatures
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Set Chart Title and Label Axis
ax.set_title("Daily High and Low Temperatures for Death Valley, Califonia 2018", fontsize=24)
ax.set_xlabel("", fontsize=14)
# Dispaly dates diagonally, call the autoformat
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=14)
# Set size of thick labels
ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()

	#for index, column_header in enumerate(header_row):
		#print(index, column_header)