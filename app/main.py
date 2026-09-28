from fastapi import FastAPI
from app.routers import tasks

app = FastAPI(title="Task Tracker API")
app.include_router(tasks.router)


@app.get("/health")
def health():
    return {"status": "ok"}
