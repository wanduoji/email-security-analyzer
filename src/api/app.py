"""FastAPI application for email security analyzer"""
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create FastAPI app
app = FastAPI(
    title="Email Security Analyzer",
    description="Enterprise-grade email security analysis system",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Import routes
from .routes import router

# Include routes
app.include_router(router, prefix="/api")

@app.get("/health", tags=["Health"])
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": "Email Security Analyzer",
        "version": "1.0.0"
    }

@app.get("/", tags=["Root"])
async def root():
    """Root endpoint"""
    return {
        "message": "Email Security Analyzer API",
        "version": "1.0.0",
        "docs": "/docs",
        "health": "/health"
    }

@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    """Global exception handler"""
    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal server error",
            "detail": str(exc) if os.getenv("DEBUG_MODE") else "An error occurred"
        }
    )
