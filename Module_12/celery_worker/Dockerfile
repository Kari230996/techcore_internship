FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --default-timeout=200 --no-cache-dir -r requirements.txt


RUN pip install celery

COPY . .

CMD ["celery", "-A", "celery_app", "worker", "--loglevel=info"]
