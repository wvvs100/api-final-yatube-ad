# API Yatube

API для публикаций, комментариев, сообществ и подписок пользователей.

## Установка

Для локального запуска используйте Python 3.10 и SQLite:

```bash
python3.10 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
cd yatube_api
python manage.py migrate
python manage.py runserver
```

Сервер будет доступен по адресу `http://127.0.0.1:8000/`, документация API —
по адресу `http://127.0.0.1:8000/redoc/`.

## Получение JWT-токена

Отправьте POST-запрос на `/api/v1/jwt/create/` с полями `username` и `password`.
Для авторизованных запросов передавайте заголовок `Authorization: Bearer <access-токен>`.

## Примеры эндпоинтов

- `GET, POST /api/v1/posts/`
- `GET, PUT, PATCH, DELETE /api/v1/posts/{post_id}/`
- `GET /api/v1/groups/`
- `GET /api/v1/posts/{post_id}/comments/`
- `GET, POST /api/v1/follow/`

### Получить JWT-токен

Запрос:

```http
POST /api/v1/jwt/create/
Content-Type: application/json
```

```json
{
  "username": "username",
  "password": "password"
}
```

Ответ содержит `access` и `refresh` токены. Для защищённых запросов отправляйте:
`Authorization: Bearer <access-токен>`.

### Создать публикацию

```http
POST /api/v1/posts/
Authorization: Bearer <access-токен>
Content-Type: application/json
```

```json
{
  "text": "Текст публикации",
  "group": 1
}
```
