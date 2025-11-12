# Используем официальный Python образ
FROM python:3.10-slim

# Устанавливаем системные зависимости
RUN apt-get update && apt-get install -y build-essential

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем зависимости
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь код проекта
COPY . .

# Указываем переменные окружения
ENV PYTHONUNBUFFERED=1

# Команда по умолчанию (для web контейнера — переопределяется в docker-compose)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
