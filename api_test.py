import requests

url = "https://ronreiter-meme-generator.p.rapidapi.com/fonts"

headers = {
    'x-rapidapi-key': "SIGN-UP-FOR-KEY",
    'x-rapidapi-host': "ronreiter-meme-generator.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)