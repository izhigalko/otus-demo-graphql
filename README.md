# Демо-проект к занятию по теме Graphql и gRPC

## Подготовка проекта

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

## Запуск GraphQL

Запустить сервис:

```shell script
python manage.py runserver
```

После запуска сервиса GraphQL интерфейс будет доступен
по [ссылке](http://127.0.0.1:8000/graphql)

### Генерация схемы

Сгенерировать GraphQL схему:

```shell script
make schema
```

## Запуск gRPC

Запустить сервис:

```shell script
python manage.py grpcserver
```

### Генерация кода из схемы

Сгенерировать код:

```shell script
make otus_graphql/books_pb2_grpc.py
```