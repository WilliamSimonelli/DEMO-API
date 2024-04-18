from fastapi import FastAPI
from routes.sample_routes import api_sample
from auth.routes import router as auth_router 

def create_app() -> FastAPI:
    app = FastAPI()

    app.include_router(auth_router)
    app.include_router(api_sample)

    return app
