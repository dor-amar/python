import requests

url = 'https://api.github.com/repos/microsoft/vscode/issues'

response = requests.get(url)

if response.status_code == 200:
    issues = response.json()
    print("Success!")
    for issue in issues:
        if issue['title'] == "MY VS CODE EDITOR IS NOT WORKING":
            break
        print(issue['title'])
else:
    print("Failed to retrieve data")

