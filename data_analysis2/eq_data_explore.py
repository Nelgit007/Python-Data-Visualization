import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Explore the data of the dataset
filename = 'data/eq_data_30_day_m1.json'
with open(filename) as f:
	eq_data = json.load(f)
	# MAke data readable to get specific info to work with
	readable_file = 'data/readable_eq_data1.json'

# To get the total count of number of earth quakes
all_eq_dictionaries = eq_data['features']
print(len(all_eq_dictionaries))

# Loop thru the dictionaries to get the magnitude, location for each earthquake
mags, lons, lats, hover_texts = [], [], [], []
for mag_locatn_eq_dictionary in all_eq_dictionaries:
	mag = mag_locatn_eq_dictionary['properties']['mag']
	lon = mag_locatn_eq_dictionary['geometry']['coordinates'][0]
	lat = mag_locatn_eq_dictionary['geometry']['coordinates'][1]
	title = mag_locatn_eq_dictionary['properties']['title']
	mags.append(mag)
	lons.append(lon)
	lats.append(lat)
	hover_texts.append(title)

#print(mags[:10])
#rint(lons[:10])
#print(lats[:10])

# Map of the earthquake affected regions
# Restructuring the list of lon & lat
data = [{
    'type': 'scattergeo',
    'text': hover_texts,
    'lon': lons,
    'lat': lats,
    # To communicate the severity of the eq we change the sizes of markers, depends
    'marker': {
        'size': [5*mag for mag in mags],
        'color': mags,
        'colorscale': 'Portland',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'},
    },
}]

my_layout = Layout(title='Globally affected Earthquake regions')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquake_Regions.html')



#with open(readable_file, 'w') as f:
	#json.dump(eq_data, f, indent=4)


