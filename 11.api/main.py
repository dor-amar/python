import requests
def categorize_jokes():
    url = "https://official-joke-api.appspot.com/jokes/random"
    categories = {}

    for x in range(10):
        response = requests.get(url)
        joke = response.json()
        joke_type = joke["type"]
        categories[joke_type] = categories.get(joke_type, 0) + 1

    print("\nJoke categories and counts:")
    for category, count in categories.items():
        print(f"{category}: {count}")

categorize_jokes()