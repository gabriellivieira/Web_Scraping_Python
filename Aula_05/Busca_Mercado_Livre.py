# Obtendo produtos do Mercado Livre a partir de uma busca
# realizada pelo usuário

import requests
from bs4 import BeautifulSoup

#Criando uma URL padrão
url_base = 'https://lista.mercadolivre.com.br/'

produto_busca = input('Informe o produto que deseja: ')

#requsição
response = requests.get(url_base + produto_busca)

site = BeautifulSoup(response.text, 'html.parser')

produto = site.find('div', attrs={'class' : 'andes-card ui-search-result ui-search-result--core andes-card--flat andes-card--padding-16'})

print(produto.prettify())