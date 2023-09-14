from bs4 import BeautifulSoup
from googlesearch import search
import requests

name = input('nome do celular:')

for dummy in search(f'hardware.com.br {name}', stop = 1):
    url = dummy
print(url)
site = requests.get(url)
soup = BeautifulSoup(site.content, 'html.parser')
scores = soup.find_all('span', {'class': 'mvalue-title'})
description = soup.find('p').get_text().strip()

print(description)

for i in range(0, len(scores)):
    if i == 0:
        print('Hardware: ', end = '')
    if i == 1:
        print('Tela: ', end = '')
    if i == 2:
        print('Camera: ', end = '')
    if i == 3:
        print('Desempenho: ', end = '')
    print(scores[i].get_text())
