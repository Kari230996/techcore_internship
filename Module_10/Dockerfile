# ========================================================
#                 BUILDER STAGE
# ========================================================
FROM python:3.10-slim AS builder

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*


WORKDIR /app

COPY requirements.txt .

RUN python3 -m venv /opt/venv

RUN /opt/venv/bin/pip install --upgrade pip && \
    /opt/venv/bin/pip install --no-cache-dir -r requirements.txt && \
    /opt/venv/bin/pip install --no-cache-dir faust-streaming aiokafka


# ========================================================
#                 FINAL STAGE
# ========================================================
FROM python:3.10-slim AS final


WORKDIR /app


COPY --from=builder /opt/venv /opt/venv


ENV PATH="/opt/venv/bin:$PATH"

COPY . .

EXPOSE 8000
EXPOSE 6066    

HEALTHCHECK --interval=20s --timeout=5s --retries=3 \
    CMD python -c "import socket; s=socket.socket(); s.connect(('localhost',8000))" || exit 1


CMD ["python", "main.py"]
