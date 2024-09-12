import requests

# Define the URL for fetching jokes
url = "https://official-joke-api.appspot.com/jokes/random"
desired_type = 'programming'

while True:
    response = requests.get(url)
    joke = response.json()
    
    # Check if the joke type matches the desired type
    if joke['type'] == desired_type:
        print(joke)
        break  # Exit the loop when a joke of the desired type is found
    else:
        print("Skipping a joke of type:", joke['type'])
