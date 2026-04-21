from fastapi import FastAPI
from app.core.database import Base, engine
from app.modules.todos.api.v1.router import router as todo_router
import os
import platform

Base.metadata.create_all(bind=engine)

description = """
Todo API helps you do awesome stuff. 🚀

## Todos

You can **create, read, update, and delete** items.
"""

tags_metadata = [
    {
        "name": "todos",
        "description": "Manage tasks and to-dos.",
    },
    {
        "name": "root",
        "description": "Root endpoint.",
    },
    {
        "name": "health",
        "description": "Health check for the service.",
    },
]

app = FastAPI(
    title="Todo API",
    description=description,
    summary="A sample Todo API showing advanced FastAPI features.",
    version="1.0.0",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "API Support",
        "url": "http://www.example.com/support",
        "email": "support@example.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
    openapi_tags=tags_metadata,
    servers=[
        {"url": "http://localhost:8000", "description": "Local Development"},
        {"url": "https://api.example.com", "description": "Production Environment"},
    ],
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
