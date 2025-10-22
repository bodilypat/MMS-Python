#run.py

import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",   # Import path to the Fastapi instance
        host="0.0.0.0",   # Listen on all interfaces
        port=8000,        # Port number
        reload=True       # Auto-reload on code changes  ( for development)
        log_level="info", # Login Level
        workers=1         # Number of worker processes 
    )