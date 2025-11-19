from fastapi import FastAPI

app = FastAPI(title="Gateway API")


@app.get("/")
def root():
    return {"message": "Gatewway is running"}


