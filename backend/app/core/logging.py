#app/core/logging.py

from logging
import logging.config 
from datetime import datetime
from typing import Optional

from fastapi import FastAPI
from app.core.config import settings

#------------------------------------------
# Log formatters
#------------------------------------------
LOG_FORMAT = (
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

AUDIT_LOG_FORMAT = (
    "%(asctime)s - AUDIT - %(message)s"
)

#------------------------------------------
# Logging Configuration
#------------------------------------------
LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,

    "formatters": {
        "default": {
            "format": LOG_FORMAT,
        },
        "audit": {
            "format": AUDIT_LOG_FORMAT,
        },
    },

    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "default",
        },
        "audit_file": {
            "class": "logging.FileHandler",
            "filename": f"logs/audit_{datetime.now().strftime('%Y%m%d')}.log",
            "formatter": "audit",
        },
    },
    "loggers": {
        "uvicorn.access": {
            "level": "INFO",
            "handlers": ["console"],
            "propagate": False,
        },
        "audit_logger": {
            "level": "INFO",
            "handlers": ["audit_file"],
            "propagate": False,
        },
    },
    "root": {
        "level": "INFO",
        "handlers": ["console"],
    },
}

#------------------------------------------
# Initialize logging
#------------------------------------------
def setup_logging():
    """Setup logging configuration."""
    logging.config.dictConfig(LOGGING_CONFIG)

#------------------------------------------
# Loggers 
#------------------------------------------
app_logger = logging.getLogger("app")
audit_logger = logging.getLogger("audit_logger")

#------------------------------------------
# Audit logging helper
#------------------------------------------
def log_audit_event(
        *,
        user_id: Optional[int],
        action: str,
        resource: str,
        resource_id: Optional[int] = None,
        request: Optional[str] = None,
        ):
    
    """Log an audit message with optional user ID."""
    audit_data = {
        "timestamp": datetime.utcnow().isoformat(),
        "user_id": user_id,
        "action": action,
        "resource": resource,
        "resource_id": resource_id,
        "ip_address": request,
        "method": request.method if request else None,
        "path": request.url.path if request else None,
    }
    audit_logger.info(audit_data)
    