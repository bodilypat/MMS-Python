# app/main.py 

""" 
    FastAPI application entry point for Medical Management System(MMS)
    Responsibilities:
    - Load environment configuration
    - Initialize logging
    - Connect database 
    - Register middleware
    - Include API routers
"""
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.core.logging import init_logging
from app.db.database import engine 
from app.models.base import Base
from app.api.v1.api_router import api_router

#--------------------------------------------
# Application Lifespan Context Manager(Start & Shoutdown )
#--------------------------------------------
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup Code
    init_logging()
    Base.metadata.create_all(bind=engine)

    app.logger.info(" MMS Backend started successfully")

    yield
    
    # Shutdown Code
    app.logger.info(" MMS Backend shutdown completed")

#--------------------------------------------
# Create FastAPI Application Instance
#--------------------------------------------
def create_app() -> FastAPI:
    app = FastAPI(
        title="Medical Management System (MMS) Backend",
        description="Backend API for Medical Management System",
        version="1.0.0",
        docs_url="/docs",
        redoc_url="/redoc",
        lifespan=lifespan
    )

    # Register Middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ALLOW_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Include API Routers
    app.include_router(api_router, prefix="/api/v1")
    return app
app = create_app()
#--------------------------------------------
# End of main.py
#--------------------------------------------