import requests

# A program that akes an APi call and stores response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
# Issue request
r = requests.get(url, headers=headers)
print(f"Status Code: {r.status_code}")

# Store API response in a dictionary variable and prints total count
response_dictionary = r.json()
print(f"{response_dictionary['total_count']}")

# Explore info about the repos
repos_dictionary = response_dictionary['items']
print(f"Repositoreis returned: {len(repos_dictionary)}")

# TASK 3
print(f"\nSelected info about each repos")
for repos in repos_dictionary:
	print(f"Name: {repos['name']}")
	print(f"Repo Owner: {repos['owner']['login']}")
	print(f"Repo Creation: {repos['created_at']}")
	print(f"Url: {repos['html_url']}")
	print(f"Stars: {repos['stargazers_count']}")
	print(f"Repo Update: {repos['updated_at']}")
	print(f"Project Description: {repos['description']}")
	print('\n')


## TASK 2
# Examining the first repo
#repos_dict = repos_dictionary[0]

# print(f"\nSelected info about a single repo [first repo]:")
# print(f"Name: {repos_dict['name']}")
# print(f"Repo Owner: {repos_dict['owner']['login']}")
# print(f"Repo Creation: {repos_dict['created_at']}")
# print(f"Url: {repos_dict['html_url']}")
# print(f"Stars: {repos_dict['stargazers_count']}")
# print(f"Repo Update: {repos_dict['updated_at']}")
# print(f"Project Description: {repos_dict['description']}")



# Examining the first repo
# repos_dict = repos_dictionary[0]
# print(f"\nKey: {len(repos_dict)}")
# for key in sorted(repos_dict.keys()):
# 	print(key)


# Store API response in a variable
#response_dictionary = r.json()

# Process the search outcomes/results.
#print(response_dictionary.keys())


# Process the search outcomes/results.
#print(response_dictionary.keys())
