# Jungle Devs - Django Challenge

## Description

**Challenge goal**: API de noticias com django rest:
 # Como instalar
 * Install [Docker](https://docs.docker.com/compose/install/)
 * Executar o comando docker

* certifique se deixar a porta 8000 liberada
```bash
docker-compose up --build
``` 
 * Criar o super usuario 
```bash
docker-compose run web python manage.py createsuperuser
```
* Seu aplicativo estará em execução em `http://127.0.0.1:8000`
- rotas comuns:
- Login API: `/api/login/`
- Sign-up API: `/api/sign-up/`
- Administrator restricted APIs:
* Para essa rotas precisa esta autenticado.
* Pata autenticar com Token JWT
- `/api/token/` passando os dados do usuario ADM
  - CRUD `/api/admin/authors/`
  - CRUD `/api/admin/articles/`
- Lista os artigos com categoria `/api/articles/?category=:slug` com a seguinte resposta:
```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": "32f26f26-d579-4d06-8375-b5445081808c",
            "author": {
                "id": "803414d4-bdcc-460b-a3b9-a154ac7e3241",
                "name": "mateus",
                "picture": "http://localhost:8000/media/author/images/perfil_6hsvzll.jpeg"
            },
            "category": {
                "name": "jogos"
            },
            "title": "Titulo do artigo",
            "summary": "resumo do artigo. resumo do artigo, resumo do artigo, resumo do artigo"
        }
    ]
}
```
- Setalhes do artigo `/api/articles/:id/` com respostas diferentes para usuários anônimos e logados:

    **Anônimo**
    ```json
        {
          "id": "95e0d270-e019-4cf9-93fc-926630432514",
          "author": {
              "id": "803414d4-bdcc-460b-a3b9-a154ac7e3241",
              "name": "mateus",
              "picture": "http://localhost:8000/media/author/images/perfil_6hsvzll.jpeg"
          },
          "category": "jogos",
          "title": "titulo",
          "summary": "summary bem grande aqui summary bem grande aqui..",
          "firstParagraph": "<p>summary bem grande aqui summary bem grande aqui summary bem grande aqui summary bem grande aqui</p>"
        }
    ```

    **Usuário logado**
    ```json
    {
      "id": "95e0d270-e019-4cf9-93fc-926630432514",
      "author": {
          "id": "803414d4-bdcc-460b-a3b9-a154ac7e3241",
          "name": "mateus",
          "picture": "http://localhost:8000/media/author/images/perfil_6hsvzll.jpeg"
      },
      "category": "jogos",
      "title": "titulo",
      "summary": "summary bem grande aqui summary bem grande aqui...",
      "firstParagraph": "<p>summary bem grande aqui..</p>",
      "body": "<div><p>summary bem grande aqui summary bem grande aqui summary bem grande aqui summary bem grande aqui</p>
      <p> summary bem grande aqui summary bem grande aqui summary bem grande aqui summary bem grande aqui</p></div>"
    }
    ```
