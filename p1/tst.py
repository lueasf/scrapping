import requests #avec un s

###
response = requests.get("https://www.google.com")
print(response.status_code)
print(response.text) # retourne le contenu de la page 
response.raise_for_status

###
url = 'https://www.jesuispaslaaa.com'
try:
    response = requests.get(url)
    response.raise_for_status()
except requests.exceptions.HTTPError as errh:
    print ("Http Error:",errh)

###
rep = requests.get("https://www.google.com")
f = open('index.html', 'w')
f.write(rep.json)