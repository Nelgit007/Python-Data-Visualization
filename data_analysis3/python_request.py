import requests

from plotly.graph_objs import Bar
from plotly import offline

# A program that akes an APi call and stores response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
# Issue request
r = requests.get(url, headers=headers)
print(f"Status Code: {r.status_code}")

# Store API response in a dictionary variable and process results
response_dictionary = r.json()
repo_dicts = response_dictionary['items']
#repo_names = []
stars, labels, repo_links = [], [], []

for repo in repo_dicts:
	#repo_names.append(repo['name'])
	# Adding links
	repo_name = repo['name']
	repo_url = repo['html_url']
	repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
	repo_links.append(repo_link)
	# Stars
	stars.append(repo['stargazers_count'])

	owner = repo['owner']['login']
	description = repo['description']
	label = f"{owner}<br />{description}"
	labels.append(label)

# Visualization
# 1. Data, 2. my_layout, 3. fig, 4. offlne
data = [{
	'type': 'bar',
	'x': repo_links	,
	'y': stars,
	'hovertext': labels,
	'marker': {
	'color': 'rgb(60,100, 150)',
	'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'},
	},
	'opacity': 0.6,
}]

my_layout = {
	'title': 'The most starred python repos in GitHub',
	'titlefont': {'size': 27},
	'xaxis': {
		'title': 'Repositories',
		'titlefont': {'size': 23},
		'tickfont': {'size': 13}},
	'yaxis': {
		'title': 'Stars',
		'titlefont': {'size': 23},
		'tickfont': {'size': 13}},
}

fig = {'data': data, 'layout': my_layout}

offline.plot(fig, filename='python_request.html')