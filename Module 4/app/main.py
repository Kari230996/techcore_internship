import time
from fastapi import FastAPI, Request

from app.routers import books


app = FastAPI(title="TechCore Internship", version="1.0")

# Middleware Логирование


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()

    print(f"{request.method} {request.url.path}")

    response = await call_next(request)

    process_time = time.time() - start_time

    print(f"{request.method} {request.url.path} завершён за {process_time:.2f}s")

    response.headers["X-Process-Time"] = str(round(process_time, 2))
    return response


app.include_router(books.router)
