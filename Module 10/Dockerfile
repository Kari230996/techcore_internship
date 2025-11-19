FROM python:3.10

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install faust-streaming aiokafka

COPY . .

CMD ["python", "main.py"]