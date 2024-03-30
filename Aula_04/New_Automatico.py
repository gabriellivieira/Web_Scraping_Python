import requests
from bs4 import BeautifulSoup
import pandas as pd

lista_noticias = []

response = requests.get('https://g1.globo.com/')

content = response.content

site = BeautifulSoup(content, 'html.parser')

noticias = site.findAll('div', attrs={'class' : 'feed-post-body'})

for noticia in noticias:
    #Titulo
    titulo = noticia.find('a', attrs={'class': 'feed-post-link'})

    #print(titulo.text)
    #print(titulo['href']) link da noticia

    #Subnoticia
    subnoticia = noticia.find('div', attrs={'class': 'bstn-fd-relatedtext'})

    if (subnoticia):
        print(subnoticia.text)
        lista_noticias.append([titulo.text, subnoticia.text, titulo['href']])
    else:
        lista_noticias.append([titulo.text, '', titulo['href']])

#Após salvar as noticias em uma lista
# Criar data frame

news = pd.DataFrame(lista_noticias, columns=['Titulo', 'Subnoticia', 'Link'])

#Salvando a lista em um arquivo CSV sem o index
news.to_csv('Noticias_03_New.csv', index=False)

#print(news)

