import router
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

tags_metadata = [
    {
        "name": "info",
        "description": "Basic server information",
    },
    {
        "name": "create",
        "description": "Endpoints used for creating new processes"
    },
    {
        "name": "manage",
        "description": "Endpoints for managing (view, kill) the processes"
    }
]

app = FastAPI(openapi_tags=tags_metadata)
app.include_router(router.router)

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title='Rest Process Spawner',
        version='1.0.0',
        description="Execute lengthy functions as processes using an API call.",
        routes=app.routes
    )

    app.openapi_schema = openapi_schema
    return app.openapi_schema


# Adding OpenAPI configuration
app.openapi = custom_openapi
