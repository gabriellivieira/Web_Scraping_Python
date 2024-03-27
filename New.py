import requests
from bs4 import BeautifulSoup

# Faz a requisição
response = requests.get('https://g1.globo.com/')

# Pega o conteúdo da requisição
content = response.content

#convertendo o objet content em html com BeautifulSoup
site = BeautifulSoup(content, 'html.parser')

#procurando a div com class feed-post-body - onde esta uma noticia
# O find trás a primeira div com o atributo do site
noticia = site.find('div', attrs={'class' : 'feed-post-body'})

# Trazer o título 
titulo = noticia.find('a', attrs={'class': 'feed-post-link'})

#Imprimir somente o titulo
print(titulo.text)

# Trazer o subnoticia
subnoticia = noticia.find('div', attrs={'class': 'bstn-fd-relatedtext'})

print(subnoticia.text)