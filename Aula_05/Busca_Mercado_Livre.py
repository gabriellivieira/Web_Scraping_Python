# Obtendo produtos do Mercado Livre a partir de uma busca
# realizada pelo usuário

import requests
from bs4 import BeautifulSoup
import pandas as pd

lista_produtos = []

#Criando uma URL padrão
url_base = 'https://lista.mercadolivre.com.br/'

produto_busca = input('Informe o produto que deseja: ')

#requsição
response = requests.get(url_base + produto_busca)

site = BeautifulSoup(response.text, 'html.parser')

produtos = site.findAll('div', attrs={'class' : 'andes-card ui-search-result ui-search-result--core andes-card--flat andes-card--padding-16'})

for produto in produtos:
    titulo = produto.find('h2', attrs={'class' : 'ui-search-item__title'})

    link = produto.find('a', attrs={'class' : 'ui-search-item__group__element ui-search-link__title-card ui-search-link'})

    real = produto.find('span', attrs={'class' : 'andes-money-amount__fraction'})
    virgula = produto.find('span', attrs={'class' : 'andes-visually-hidden'})
    centavos = produto.find('span', attrs={'class' : 'andes-money-amount__cents'})

    #print(produto.prettify())
    print('Titulo do produto:', titulo.text)
    print('Link do prodto:', link['href'])

    if (centavos):
        lista_produtos.append([titulo.text, link['href'], real.text + virgula.text + centavos.text])
        print('Preço do produto: R$', real.text + virgula.text + centavos.text)
    else:
        lista_produtos.append([titulo.text, link['href'], real.text])
        print('Preço do produto: R$', real.text)

    print ('\n\n')


#Lista para impressão
lista = pd.DataFrame(lista_produtos, columns=['Titulo', 'Link', 'Real'])

lista.to_csv('Produtos_Mercado_Livre.csv', index=False)