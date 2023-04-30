![yamdb_final event parameter](https://github.com/o5c1ll47or/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg?event=push)

# Проект YaMDb

Проект YaMDb собирает отзывы пользователей на произведения. Произведения делятся на категории: «Книги», «Фильмы», «Музыка». В каждой категории есть произведения: книги, фильмы или музыка. Произведению может быть присвоен жанр. Новые жанры может создавать только администратор. Пользователи могут оставить к произведениям текстовые отзывы и поставить произведению оценку (в диапазоне от одного до десяти). Из пользовательских оценок формируется усреднённая оценка произведения — рейтинг.

Аутентификация по JWT-токену.
Поддерживает методы GET, POST, PUT, PATCH, DELETE.
Предоставляет данные в формате JSON.
Создан в команде из трех человек с использованием Git в рамках учебного курса Яндекс.Практикум.

 ## Стек технологий

![python version](https://img.shields.io/badge/Python-3.7-yellowgreen) 
![python version](https://img.shields.io/badge/Django-3.2-yellowgreen) 
![python version](https://img.shields.io/badge/djangorestframework-3.12.4-yellowgreen) 
![python version](https://img.shields.io/badge/djangorestframework--simplejwt-4.7.2-yellowgreen) 

## Ресурсы API YaMDb

* Ресурс auth: аутентификация.
* Ресурс users: пользователи.
* Ресурс titles: произведения, к которым пишут отзывы (определённый фильм, книга или песенка).
* Ресурс categories: категории (типы) произведений («Фильмы», «Книги», «Музыка»).
* Ресурс genres: жанры произведений. Одно произведение может быть привязано к нескольким жанрам.
* Ресурс reviews: отзывы на произведения. Отзыв привязан к определённому произведению.
* Ресурс comments: комментарии к отзывам. Комментарий привязан к определённому отзыву.

## Как запустить проект

Клонировать репозиторий:

```
git clone https://github.com/o5c1ll47or/yamdb_final.git
```

Перейти в папку infra и запустить docker-compose.yaml
(при установленном и запущенном Docker)
```
cd yamdb_final/infra
docker-compose up
```

Для пересборки контейнеров выполнять команду:
(находясь в папке infra, при запущенном Docker)
```
docker-compose up -d --build
```

В контейнере web выполнить миграции:

```
docker-compose exec web python manage.py migrate
```

Создать суперпользователя:

```
docker-compose exec web python manage.py createsuperuser
```

Собрать статику:

```
docker-compose exec web python manage.py collectstatic --no-input
```

Проверьте работоспособность приложения, для этого перейдите на страницу:

```
http://localhost/admin/
```

## Документация к проекту

Документация для API после установки доступна по адресу 

```http://127.0.0.1/redoc/```
