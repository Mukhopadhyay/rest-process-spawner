import router
from fastapi import FastAPI

tags_metadata = [
    {
        "name": "info",
        "description": "Basic server information",
    },
    {
        "name": "processes",
        "description": "Endpoints related to managing active processes"
    }
]

app = FastAPI(openapi_tags=tags_metadata)
app.include_router(router.router)
