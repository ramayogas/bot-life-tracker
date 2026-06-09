from fastapi import FastAPI
from app.db.session import engine, Base
from app.routes import health

app = FastAPI(title="Life Tracker Bot API")

# create tables
Base.metadata.create_all(bind=engine)

app.include_router(health.router)


@app.get("/")
def root():
    return {"message": "Life Tracker API is running"}