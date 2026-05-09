#!/usr/bin/env python3
"""
Render deployment debugging and logging
"""

import logging
import os
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

logger.info("=== Render Environment Debug ===")
logger.info(f"FLASK_CONFIG: {os.getenv('FLASK_CONFIG', 'Not set')}")
logger.info(f"SECRET_KEY: {'Set' if os.getenv('SECRET_KEY') else 'Not set'}")
logger.info(f"DATABASE_URL: {'Set' if os.getenv('DATABASE_URL') else 'Not set'}")
logger.info(f"DB_USER: {os.getenv('DB_USER', 'Not set')}")
logger.info(f"DB_HOST: {os.getenv('DB_HOST', 'Not set')}")
logger.info(f"DB_PORT: {os.getenv('DB_PORT', 'Not set')}")
logger.info(f"DB_NAME: {os.getenv('DB_NAME', 'Not set')}")
logger.info(f"USE_SQLITE: {os.getenv('USE_SQLITE', 'Not set')}")

# Test database connection
try:
    from app import app, db
    with app.app_context():
        result = db.engine.execute("SELECT 1")
        logger.info("✅ Database connection successful!")
except Exception as e:
    logger.error(f"❌ Database connection failed: {e}")
    logger.error(f"Error type: {type(e).__name__}")
    import traceback
    logger.error(f"Traceback: {traceback.format_exc()}")

logger.info("\n=== Common Render Issues ===")
logger.info("1. DATABASE_URL not properly set in environment")
logger.info("2. PostgreSQL connection string format error")
logger.info("3. Database not accessible from Render network")
logger.info("4. Missing required environment variables")
