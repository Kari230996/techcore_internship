
---

# 🧑‍💻 TechCore Internship — Backend Python Developer

## 📌 Общая информация

Данный репозиторий содержит результаты **обучаемой стажировки Backend Python Developer** в компании **TechCore**.

Стажировка была построена в формате **последовательных практических модулей**, каждый из которых расширял систему и углублял знания в области:

* Backend-разработки
* микросервисной архитектуры
* контейнеризации
* асинхронных задач
* мониторинга и наблюдаемости
* Kubernetes и production-подходов

Проект развивался **итеративно**, от простого REST API до системы с:

* Kafka
* Celery
* Redis
* OpenTelemetry
* Prometheus / Grafana / Loki
* Kubernetes (Ingress, Canary, ServiceMonitor)

---

## 🏗 Архитектура проекта

* **Backend**: Python, FastAPI
* **База данных**: PostgreSQL
* **Асинхронность**: Celery, Kafka
* **Кэш / брокеры**: Redis
* **Контейнеризация**: Docker, Docker Compose
* **Оркестрация**: Kubernetes (Minikube)
* **Мониторинг**: Prometheus, Grafana
* **Трейсинг**: OpenTelemetry, Jaeger
* **Логирование**: Loki

---

## 📚 Структура стажировки по модулям

---

### 🔹 Модуль 1 — Основы Python и Настройка Окружения

**Задача:**
[https://portal.techcoredev.ru/extranet/workgroups/group/5/tasks/task/view/271/](https://portal.techcoredev.ru/extranet/workgroups/group/5/tasks/task/view/271/)

**Что сделано:**

* Настройка виртуального окружения и зависимостей
* Базовый синтаксис Python
* Работа со структурами данных
* Файлы, JSON, HTTP и обработка ошибок

---

### 🔹 Модуль 2 — Продвинутый Python (OOP, multiprocessing и Генераторы)

**Задача:**
[https://portal.techcoredev.ru/extranet/workgroups/group/5/tasks/task/view/273/](https://portal.techcoredev.ru/extranet/workgroups/group/5/tasks/task/view/273/)

**Что сделано:**

* Основы ООП в Python
* Декораторы, генераторы, контекстные менеджеры
* Разница между threading и multiprocessing (GIL)
* Параллельные вычисления с multiprocessing


---

### 🔹 Модуль 3 — asyncio (Асинхронное Программирование)

**Задача:**
[https://portal.techcoredev.ru/extranet/workgroups/group/5/tasks/task/view/275/](https://portal.techcoredev.ru/extranet/workgroups/group/5/tasks/task/view/275/)

**Что сделано:**


* Изучена работа `asyncio` и Event Loop
* Написаны асинхронные функции с `async/await`
* Реализовано параллельное I/O (gather, HTTP, очереди)
* Асинхронная работа с файлами и блокирующим кодом


---

### 🔹 Модуль 4 — Web Framework (FastAPI)

**Задача:**
[https://portal.techcoredev.ru/extranet/workgroups/group/5/tasks/task/view/277/](https://portal.techcoredev.ru/extranet/workgroups/group/5/tasks/task/view/277/)

**Что сделано:**

* Создан REST API на **FastAPI** (запуск, роуты, async)
* Использованы **Pydantic-схемы** и автоматическая валидация
* Реализован **CRUD**, обработка ошибок и DI (`Depends`)
* Подключены роутеры, middleware и Swagger-документация


---

### 🔹 Модуль 5 — SQL (SQLAlchemy и Alembic)

**Задача:**
[https://portal.techcoredev.ru/extranet/workgroups/group/5/tasks/task/view/279/](https://portal.techcoredev.ru/extranet/workgroups/group/5/tasks/task/view/279/)

**Что сделано:**

* Поднята **PostgreSQL** через Docker Compose
* Описаны модели и миграции (**SQLAlchemy + Alembic**)
* Настроена **асинхронная работа с БД**
* Реализован CRUD, связи и транзакции


---

### 🔹 Модуль 6 — NoSQL (Redis и MongoDB)

**Задача:**
[https://portal.techcoredev.ru/extranet/workgroups/group/5/tasks/task/view/281/](https://portal.techcoredev.ru/extranet/workgroups/group/5/tasks/task/view/281/)

**Что сделано:**

* Подключены **Redis и MongoDB** через Docker
* Реализовано **асинхронное кэширование** и инвалидация
* CRUD и сервисы на **MongoDB (Motor)**
* Параллельный сбор данных и Redis-блокировки

---

### 🔹 Модуль 7 — Тестирование (Pytest)

**Задача:**
[https://portal.techcoredev.ru/extranet/workgroups/group/5/tasks/task/view/283/](https://portal.techcoredev.ru/extranet/workgroups/group/5/tasks/task/view/283/)

**Что сделано:**

* Юнит-тесты и фикстуры с **pytest**
* Моки сервисов и репозиториев
* Интеграционные и async-тесты FastAPI
* E2E-тесты в Docker и покрытие кода


---

### 🔹 Модуль 8 — HTTP Клиенты и Отказоустойчивость (HTTPX и asyncio)

**Задача:**
[https://portal.techcoredev.ru/extranet/workgroups/group/5/tasks/task/view/285/](https://portal.techcoredev.ru/extranet/workgroups/group/5/tasks/task/view/285/)

**Что сделано:**

* Асинхронные HTTP-клиенты (**httpx**)
* Таймауты, ретраи и Circuit Breaker
* Ограничение нагрузки и fallback-ответы
* Параллельные вызовы и альтернативы (aiohttp, gRPC)

---

### 🔹 Модуль 9 — Message Bus (Celery и RabbitMQ)

**Задача:**
[https://portal.techcoredev.ru/extranet/workgroups/group/5/tasks/task/view/287/](https://portal.techcoredev.ru/extranet/workgroups/group/5/tasks/task/view/287/)

**Что сделано:**

* Настроены **Celery и RabbitMQ**
* Асинхронная обработка фоновых задач
* Ретраи, DLQ и планировщик задач
* Мониторинг и workflow (Flower, chains)


---

### 🔹 Модуль 10 — Event Streaming (Kafka)

**Задача:**
[https://portal.techcoredev.ru/extranet/workgroups/group/5/tasks/task/view/289/](https://portal.techcoredev.ru/extranet/workgroups/group/5/tasks/task/view/289/)

**Что сделано:**

* Настроен **Kafka** для потоковых событий
* Реализованы **producer и consumer**
* Сбор аналитики и масштабирование воркеров
* Гарантии доставки и async-обработка

---

### 🔹 Модуль 11 — Полный Стек (docker-compose и FastAPI Gateway)

**Задача:**
[https://portal.techcoredev.ru/extranet/workgroups/group/5/tasks/task/view/291/](https://portal.techcoredev.ru/extranet/workgroups/group/5/tasks/task/view/291/)

**Что сделано:**

* Собран полный стек сервисов в **docker-compose**
* Созданы Dockerfile и контейнеры FastAPI
* Реализован **API Gateway** (маршрутизация, auth)
* Агрегация запросов и сервис-дискавери


---

### 🔹 Модуль 12 — Observability (Мониторинг docker-compose стека)

**Задача:**
[https://portal.techcoredev.ru/extranet/workgroups/group/5/tasks/task/view/293/](https://portal.techcoredev.ru/extranet/workgroups/group/5/tasks/task/view/293/)

**Что сделано:**

* Подключена **observability** (OpenTelemetry)
* Трейсинг запросов через **Zipkin**
* Метрики и дашборды (**Prometheus + Grafana**)
* Централизованные логи и мониторинг воркеров


---

### 🔹 Модуль 13 — Миграция в Kubernetes: Основы (Minikube)

**Задача:**
[https://portal.techcoredev.ru/extranet/workgroups/group/5/tasks/task/view/295/](https://portal.techcoredev.ru/extranet/workgroups/group/5/tasks/task/view/295/)

**Что сделано:**

* Развёрнут **Minikube** и базовые ресурсы Kubernetes
* Перенос FastAPI + Postgres в **K8s**
* Использование **ConfigMap, Secret и PVC**
* Деплой и доступ к сервису через NodePort


---

### 🔹 Модуль 14 — Миграция в Kubernetes: Продвинутый Стек (Helm и Ingress)

**Задача:**
[https://portal.techcoredev.ru/extranet/workgroups/group/5/tasks/task/view/297/](https://portal.techcoredev.ru/extranet/workgroups/group/5/tasks/task/view/297/)

**Что сделано:**

* Развёртывание инфраструктуры в **Kubernetes через Helm**
* Деплой всех Python-сервисов в K8s
* Настройка **Ingress** и сервис-дискавери
* Health-checks и автоматическое восстановление


---

### 🔹 Модуль 15 — Observability и CI/CD в Kubernetes

**Задача:**
[https://portal.techcoredev.ru/extranet/workgroups/group/5/tasks/task/view/299/](https://portal.techcoredev.ru/extranet/workgroups/group/5/tasks/task/view/299/)

**Что сделано:**

* Мониторинг Kubernetes (**Prometheus, Grafana, Loki, Jaeger**)
* Метрики и трейсы Python-сервисов
* CI/CD через **GitHub Actions**
* Автодеплой и канареечные релизы

---

## 🎯 Итог

В рамках стажировки был реализован **полноценный backend-сервис**, прошедший путь:

> от простого API → до production-ready микросервиса

Стажировка дала практический опыт:

* реальной backend-разработки
* работы с инфраструктурой
* понимания production-паттернов
* анализа и отладки сложных систем

---

