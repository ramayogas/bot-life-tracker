from fastapi import FastAPI
from app.db.session import engine, Base
from app.routes import health
from app.routes import user
from app.routes import finance
from app.routes import daily

app = FastAPI(title="Life Tracker Bot API")

# create tables
Base.metadata.create_all(bind=engine)

app.include_router(health.router)
app.include_router(user.router)
app.include_router(finance.router)
app.include_router(daily.router)


@app.get("/")
def root():
    return {"message": "Life Tracker API is running"}