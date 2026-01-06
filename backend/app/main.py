#app/main.py
"""
   FastAPI application entry point for Medical Management System (MMS)
   Responsibilities:
      Load environment configuration
      Initialize logging 
      Manage application lifespan
      Initialize database 
      Register middleware 
      Include API routers 
"""

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.core.logging import init_logging
from app.db.database import engine 
from app.models.base import Base 
from app.api.v1.api_router import api_router

#-----------------------------------------
# Application lifespan (Startup and Shutdown)
#-----------------------------------------
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup actions
    init_logging()

    try: 
        Base.metadata.create_all(bind=engine)
        app.logger.info("Database connected and tables eensured.")
    except Exception as e:
        app.logger.error(f"Database connection failed: {e}")
        raise e
    
    app.logger.info("Application startup complete.")

    yield
    
    # Shutdown actions (if any)
    app.logger.info("Application shutdown complete.")

#-----------------------------------------
# FastAPI Application Factory
#-----------------------------------------
def create_app() -> FastAPI:
    app = FastAPI(
        title="Medical Management System (MMS) Backend",
        description="Backend API for managing medical records, appointments, and patient data.",
        version="1.0.0",
        docs_url="/docs",
        redoc_url="/redoc",
        lifespan=lifespan,
        openapi_url="/openapi.json",
    )

#-----------------------------------------
# Middleware 
#-----------------------------------------
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

#-----------------------------------------
# API Routers
#-----------------------------------------
    app.include_router(api_router, prefix="/api/v1")
    return app
#-----------------------------------------
# ASGI Application 
#-----------------------------------------
app = create_app()

