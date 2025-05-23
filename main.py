from fastapi import FastAPI
from endpoints import posts, auth
from starlette.middleware.sessions import SessionMiddleware
import os
from db.database import Base, engine

app = FastAPI()

app.add_middleware(SessionMiddleware, secret_key=os.getenv("SESSION_SECRET_KEY"))

Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(posts.roter)