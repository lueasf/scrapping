import requests
from bs4 import BeautifulSoup
from pprint import pprint

url = "https://books.toscrape.com/"
rep = requests.get(url)

soup = BeautifulSoup(rep.text, 'html.parser')   #type de parseur/3, html.parser, html5lib
#print(soup.prettify())
img = soup.find_all('img')
#pprint(img)
aside =soup.find('div', class_='side_categories')
categ_div = aside.find('ul').find('li').find('ul')
categ = [child.text.strip() for child in categ_div.children if child.name =='li']
#pprint(categ)

images = soup.find_all('img')
for image in images:
    print(image['src']) #nom de l'attr