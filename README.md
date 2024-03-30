
# Web Scraping com Python

Percorre as páginas web buscando informações atrás de "raspagens de rede" em tradução livre, também é conhecido por realizar extração de dados da web, é o nome dado ao processo de coleta de dados estruturados da web de forma automatizada. 

Se utiliza da estrutura HTML de um site e suas funções para percorrer o site em específico e viabilizar a coleta de dados. 

O HTML (Hyper Text Markup Language) possui marcações em tags, no qual em cada tag delimitada por < > possui uma área da pagina, assim o HTML delimita cada parte de uma parte da página com uma tag de abertura ( <> ) e fechamento ( </> )exemplo:

~~~~
<html> - onde inicia o documento

<head> - o cabeçalho do documentos entre outros.
~~~~

## Protocolo HTTP
Protocolo de interconexão de redes de computadores, que padroniza o envio e recebimento de informações. É uma forma convencionada para mostrar como as coisas devem funcionar. 
O HTTP (HyperText transfer Protocol) define o modo como as coisas são acessadas na web.
As respostas das requisições são Strings padronizadas, assim quando é feito uma requisição em Python (ou outra linguagem) a resposta virá em: Código de status, cabeçalho e conteúdo. 

* Códigos de Status
	Informativo (1XX) - resposta sem conteúdo, contem informações sobre comunicação
	Sucesso (2XX) - A mensagem chegou ao servidor e era válido
	Redirecionamento (3XX) - O recurso buscado esta em outro servidor
	Erro do cliente (4XX) - A requisição possui algum erro
	Erro do servidor (5XX) - O servidor não pode atender à requisição



### Um dos métodos HTTP são:
* GET: solicita um recurso para servidor (uma página da web, por exemplo);
* POST: Enviamos uma informação para o servidor, como, por exemplo, um login onde é feito o envio dos dados de acesso que serão verificados. 

## Agradecimento
Agradeço ao professor [Walisson Silva](https://github.com/walissonsilva) por compartilhar seus conhecimentos no YouTube e pelos repositórios no GitGub.

