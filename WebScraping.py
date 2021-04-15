# Scraping github to extract user name and profile picture

from bs4 import BeautifulSoup
import requests

username = input('Enter your github username: \n')
github_url = 'https://github.com/' + username

data_request = requests.get(github_url)

soup = BeautifulSoup(data_request.content, 'html.parser')

profile_picture = soup.find('img', {'style': 'height:auto;'})['src']
user_name = soup.find(class_='p-name').get_text()

print(user_name)
print(profile_picture)
