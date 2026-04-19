from fastapi import FastAPI

from app.api import health

app = FastAPI(title="RAG Product Search", version="0.1.0")

app.include_router(health.router)


@app.get("/")
def root() -> dict[str, str]:
    return {"service": "rag-product-search", "docs": "/docs"}
