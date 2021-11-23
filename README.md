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

Com o Docker e Docker Compose instalado, execute o seguinte comando na raiz do projeto:

```
docker-compose up -d
```

Você poderá acessar a aplicação atráves do endereço abaixo direto no seu navegador:

```
http://localhost:49160/
```

Em seguida basta escolher um gênero de filme disponível para receber uma lista de filmes de acordo com sua escolha!
