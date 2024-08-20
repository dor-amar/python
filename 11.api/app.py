import requests

# Define the URL for fetching ten jokes
url = "https://official-joke-api.appspot.com/jokes/ten"

# Make a GET request to the API
response = requests.get(url)

jokes = response.json()

print(jokes)
