import json, requests

# Making a get request to get the latest position of the international space station from the opennotify api.

response = requests.get("http://api.open-notify.org/iss-now.json")
status_code = response.status_code

# The ISS Pass endpoint returns when the ISS will next pass over a given location on earth. In order to compute this, we need to pass the coordinates of the location to the API.

# This is the latitude and longitude of New York City.
parameters = {"lat": 37.78, "lon": -122.41}
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
content = response.content

#Working with JSON using Python support

best_food_chains = ["Taco Bell", "Shake Shack", "Chipotle"]
print(type(best_food_chains))

# Use json.dumps to convert best_food_chains to a string.
best_food_chains_string = json.dumps(best_food_chains)
print(type(best_food_chains_string))

# Convert best_food_chains_string back into a list
print(type(json.loads(best_food_chains_string)))

#Getting JSON from a request

parameters = {"lat": 37.78, "lon": -122.41}
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

# Get the response data as a python object.  Verify that it's a dictionary.
data = response.json()
#print(type(data))
#print(data)
first_pass = data["response"][0]
print(first_pass)
first_pass_duration = first_pass['duration']

#Finding the number of people in space

response = requests.get("http://api.open-notify.org/astros.json")
data = response.json()
print(data)
in_space_count = data['number']

#API Authentication

headers = {"Authorization": "token generated_token"}
response = requests.get("https://api.github.com/users/VikParuchuri/orgs", headers=headers)
print(response.json())
orgs = response.json()

#Pagination

params = {"per_page": 50, "page": 2}
response = requests.get("https://api.github.com/users/VikParuchuri/starred", headers=headers, params=params)
page2_repos = response.json()

#POST Requests

payload = {"name": "learning-about-apis"}
response = requests.post("https://api.github.com/user/repos", json=payload, headers=headers)
status = response.status_code

#PUT/PACTH requests
payload = {"description": "Learning about requests!", "name": "learning-about-apis"}
response = requests.patch("https://api.github.com/repos/VikParuchuri/learning-about-apis", json=payload, headers=headers)
status = response.status_code


