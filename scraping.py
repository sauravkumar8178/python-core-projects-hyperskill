from bs4 import BeautifulSoup
import requests
url = 'https://www.linkedin.com/company/example'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
name = soup.find('h1', {'class': 'org-top-card-summary__title'}).text
description = soup.find('div', {'class': 'org-about-us-organization-description__text'}).text
