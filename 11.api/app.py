import requests

# Code
# response = requests.get('https://randomfox.ca/floof/')

# print(response.status_code)
# print(type(response.json()))
# print(response.json())

# Jokes api 

# url = 'https://official-joke-api.appspot.com/random_joke'

# response = requests.get(url)
# joke = response.json()

# print(joke)
# print(joke['setup'], joke['punchline'])

# Github 
                    
# url = 'https://api.github.com/repos/microsoft/vscode/issues'
# response = requests.get(url)
# issues = response.json()

# for issue in issues:
#     print(issue['title'])


# Working with status code 
# url = 'https://api.github.com/reposgfdbgf/microsoft/vscode/issues'
# response = requests.get(url)

# if response.status_code == 200:
#     print("Success")
#     data = response.json()
#     print(data[1]['title'])
#     print(data[1]['repository_url'])

# else:
#     print(response.status_code)

# url = 'https://jsonplaceholder.typicode.com/posts'
# data = {'title': 'dor','body':'hello','userId': 1}

# x = requests.post(url, data= data) 
# print(x.status_code)

# url = 'https://official-joke-api.appspot.com/jokes/ten'
# resoponse = requests.get(url)

# if resoponse.status_code == 200: 
#   jokes = resoponse.json()
#   for joke in jokes:
#     print(f"{joke['setup']} - {joke['punchline']}")
# else: 
#   print(resoponse.status_code)

#Sahar 

# url = "https://jsonplaceholder.typicode.com/posts"
# data = {
#     "title": "My New Post",
#     "body": "This is the content of my new post.",
#     "userId": 1000
# }
# response = requests.post(url, json=data)

# if response.status_code == 201:
#   new_post = response.json()
#   print(f"Post created successfully! New post ID: {new_post}")
# else:
#   print(f"Error: {response.status_code}")

# Exercise 2 

def rating_jokes():
    url = 'https://official-joke-api.appspot.com/jokes/random'
    joke_rating = {}

    for i in range(10):
      response = requests.get(url)
      joke = response.json()
      print(joke) # Print Joke 

      # Logic
      rating = int(input("Enter joke rating"))
      joke_rating[i+1] = rating

    avrage_rating = sum(joke_rating.values()) / len(joke_rating)
    print(avrage_rating)


rating_jokes()







   