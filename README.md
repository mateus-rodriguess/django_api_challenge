# Django Challenge

## Description
News API with Django REST framework

## Development environment
### Tools needed:
 * Install [Docker](https://docs.docker.com/compose/install/)
  * Make sure you leave port 8000 open
  * Run docker command in project root
    ```bash
      docker-compose up --build
    ``` 
 * Create the super user to access the CRUD routes
    ```bash
     docker exec -it challenge_web bash
     python manage.py createsuperuser
    ```

* Your application will be running on `http://127.0.0.1:8000`
* There is a `Postman collection` that is in the repository, with all the routes mapped 
## Production environment
Environment Variables
Rename ```.env.dev ``` to ```.env``` and configure in django_challenge/settings.py:
 * SECRET_KEY
 * ``` python
       import secrets
       secrets.token_urlsafe(60) 
   ```
* Start container
  ` docker-compose -f docker-compose-dev.yml up `
* Container access
  ` docker-compose -f docker-compose-dev.yml exec challenge_web bash `
* Create super user
  ` python manage.py createsuperuser `

# Endpoint login and authentication
 * Rotas comuns:
    - Login API: `/api/login/`
    - Sign-up API: `/api/sign-up/`
    - Get token: `/api/token/`

 - Admin restricted APIs:
 - Articles
   - CREATE - `/api/admin/articles/create/`
   - UPDATE - `/api/admin/articles/update/<id>/`
   - DELETE - `/api/admin/articles/delete/<id>/`
 - Category
   - CREATE - `/api/admin/category/create/`
   - UPDATE - `/api/admin/category/update/<id>/`
   - DELETE - `/api/admin/category/delete/<id>/`
 - Author
   - CREATE - `/api/admin/author/create/`
   - UPDATE - `/api/admin/author/update/<id>/`
   - DELETE - `/api/admin/author/delete/<id>/`
 - User
   - LIST - `api/admin/accounts/`
 
- Endpoint
- List articles with category `/api/articles?category=<slug>` with the following answer:
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
- Article details `/api/articles/<id>/` with different answers for anonymous and logged in users:

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

    **Logged user**
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
        "firstParagraph": "<p>summary bem grande aqui..</p>"
      }
     ```
     # endpoint category
     - Category - `/api/category/ `
        ``` json
           {
             "count": 1,
             "next": null,
             "previous": null,
             "results": [
                 {
                     "id": "06833173-3e53-415a-91eb-d528cd48dbf9",
                     "name": "category"
                 }
             ]
           }
        ```
     - Category id - `/api/category/<id>/ `
         ```json 
           {
              "id": "06833173-3e53-415a-91eb-d528cd48dbf9",
             "name": "category"

           }
         ```
   
