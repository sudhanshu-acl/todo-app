from fastapi import FastAPI
from app.core.database import Base, engine
from app.modules.todos.api.v1.router import router as todo_router
from app.core.docs import description, tags_metadata, contact_info, license_info, servers
import os
import platform
from fastapi.middleware.cors import CORSMiddleware
from typing import Annotated

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Todo API",
    description=description,
    summary="A sample Todo API showing advanced FastAPI features.",
    version="1.0.0",
    terms_of_service="http://example.com/terms/",
    contact=contact_info,
    license_info=license_info,
    openapi_tags=tags_metadata,
    servers=servers,
)

origins = [
    "http://localhost:8000",  # frontend URL
    "http://127.0.0.1:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,   # or ["*"] for testing
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["root"])
def read_root():
    return {
        "detail": "Todo API v1.0 - Visit /docs for interactive UI or /todos/ for todos endpoints.",
        "description": "Todo API v1.0 - Visit /docs for interactive UI or /todos/ for todos endpoints."
    }

@app.get("/health", tags=["health"])
def health_check():
    return {
        "status": "ok",
        "environment": os.getenv("ENV", "not set"),
        "cwd": os.getcwd(),
        "system": {
            "os": platform.system(),
            "os_version": platform.version(),
            "platform": platform.platform(),
            "python_version": platform.python_version(),
            "hostname": platform.node(),
            "cpu_count": os.cpu_count()
        }
    }

app.include_router(todo_router)
