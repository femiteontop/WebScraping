# Scraping github to extract profile picture

from bs4 import BeautifulSoup
import requests

username = input('Enter your github username: \n')
github_url = 'https://github.com/' + username

data_request = requests.get(github_url)

soup = BeautifulSoup(data_request.content, 'html.parser')

profile_picture = soup.find('img', {'style': 'height:auto;'})['src']

print(f"Follow below link to {username}'s Github profile picture")
print(profile_picture)
