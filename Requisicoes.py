import requests

#requisição do tipo Get por meio do modulo request instalado pelo Jupyter Notebook

response = requests.get('https://www.daxpatterns.com/statistical-patterns/')

print('Status code:', response.status_code)
print(' ** HEADER **')
print(response.headers)

print("\n ** Content **")
print(response.content)