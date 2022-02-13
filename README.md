# Django Challenge

## Description
API de noticias com django rest:

## Ambiente de desenvolvimento
### Ferramentas necessárias:
 * Install [Docker](https://docs.docker.com/compose/install/)
  * certifique se deixar a porta 8000 liberada
  * Executar o comando docker na raiz do projeto
```bash
docker-compose -d up --build
``` 
 * Criar o super usuario para acessar as rotas de CRUD 
```bash
 docker exec -it challenge_web bash
 python manage.py createsuperuseruser
```

* Seu aplicativo estará em execução em `http://127.0.0.1:8000`
* Tem uma Postman collection que esta no repositirio, comas rotas mapeadas
# Rotas 
- rotas comuns:
- Login API: `/api/login/`
- Sign-up API: `/api/sign-up/`
- Obter token: `/api/token/`
 
- APIs restritas ao administrador:
  - Articles
   - CREATE - `/api/admin/articles/create/`
   - update - `/api/admin/articles/update/<id>/`
   - delete - `/api/admin/articles/delete/<id>/`
- Category
  - create - `/api/admin/category/create/`
  - update - `/api/admin/category/update/<id>/`
  - delete - `/api/admin/category/delete/<id>/`
- Author
  - create - `/api/admin/author/create/`
  - update - `/api/admin/author/update/<id>/`
  - delete - `/api/admin/author/delete/<id>/`

- Rotas comuns
- Lista os artigos com categoria `/api/articles?category=<slug>` com a seguinte resposta:
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
