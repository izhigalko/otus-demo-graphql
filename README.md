# Демо-проект к занятию по теме Graphql

## Запуск проекта

Установить зависимости:

```shell script
pip install -r requirements.txt
```

Запустить миграцию данных:

```shell script
python manage.py migrate
```

Загрузить тестовый набор данных:

```shell script
python manage.py loaddata books
```

Запустить сервис

```shell script
python manage.py runserver
```

После запуска сервиса GraphQL интерфейс будет доступен
по [ссылке](http://127.0.0.1:8000/graphql)

## Генерация схемы

Сгенерировать GraphQL схему:

```shell script
make schema
```
