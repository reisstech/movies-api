# Movies API - Uma API desenvolvida em NodeJS e Python para encontrar filmes de acordo com o seu gosto :)

API desenvolvida usando o conceito de Microserviços.

Consiste em uma API em NodeJs usando Express e outra usando Python Flask, cada uma rodando em um container Docker diferente.
A aplicação em Node fica reponsável por receber a requisição do usuário com o gênero de filme escolhido e chamar uma rota na API Flask que por sua vez irá
fazer a requisição para a API externa do The Movie DB. A API externa retorna a requisição com um JSON com os filmes encontrados com o gênero escolhido pelo usuário.

## Tecnologias usadas

* **NodeJS**
*  **Express**
*  **Python**
*  **Flask**
*  **Docker**

## Como usar

Faça o clone do repositório:

```
git clone https://github.com/reisstech/movies-api.git
```

Com o Docker e Docker Compose instalado, execute o seguinte comando na raiz do projeto:

```
docker-compose up -d
```

Você poderá acessar a aplicação atráves do endereço abaixo direto no seu navegador:

```
http://localhost:49160/
```
Obs: Se por algum motivo você queira alterar a porta onde a aplicação irá rodar. Basta setar no arquivo .env a porta desejada.

```
.env

NODEJS_PORT=PORTA DESEJADA
```

Na página inicial do site, basta escolher um gênero de filme disponível para receber uma lista em JSON de filmes de acordo com sua escolha!

Deixei a API em Flask exposta na porta 49161 para fim de testes, mas não havia necessidade. Visto de que quem recebe e entrega o que foi solicitado pelo usuário
final é a API Node Express.
