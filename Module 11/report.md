# Добавление сервисов в docker-compose

## Выполненные задачи

* Добавлен сервис **book-service (FastAPI)**
* Добавлен **order-worker (Celery)**
* Добавлен **analytics-worker (Kafka Consumer)**
* Все сервисы интегрированы через общий `docker-compose.yml`
* Для всех сервисов используется `build: .` и собственные Dockerfile
* Добавлены зависимости от инфраструктурных сервисов (Kafka, Redis, PostgreSQL, RabbitMQ)

## Проверка работы

Команда:

```bash
docker-compose up --build
```

успешно собирает и запускает все контейнеры.

## Запущенные контейнеры

В рабочем окружении поднимается **14 контейнеров**, включая:

* FastAPI (book-service)
* Celery worker (order-worker)
* Celery beat
* Kafka analytics workers (sync + async)
* Kafka producer
* Faust worker
* PostgreSQL
* Redis
* MongoDB
* RabbitMQ
* Kafka
* Zookeeper
* Zipkin
* Flower

Все контейнеры находятся в статусе **Up** или **Up (healthy)**.

## Итог

Критерий приёмки выполнен:

> `docker-compose up --build` собирает и запускает **10+ контейнеров**.




