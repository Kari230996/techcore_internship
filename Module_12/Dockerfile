FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --default-timeout=200 --no-cache-dir -r requirements.txt


COPY . .

CMD ["python", "analytics_worker.py"]
