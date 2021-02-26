import requests

response = requests.get("https://uselessfacts.jsph.pl/random.json?language=en")
print(response.json()["text"])