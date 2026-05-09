#!/usr/bin/env python3
"""
Debug script for Render deployment issues
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

print("=== Render Environment Debug ===")
print(f"FLASK_CONFIG: {os.getenv('FLASK_CONFIG', 'Not set')}")
print(f"SECRET_KEY: {'Set' if os.getenv('SECRET_KEY') else 'Not set'}")
print(f"DATABASE_URL: {'Set' if os.getenv('DATABASE_URL') else 'Not set'}")
print(f"DB_USER: {os.getenv('DB_USER', 'Not set')}")
print(f"DB_HOST: {os.getenv('DB_HOST', 'Not set')}")
print(f"DB_PORT: {os.getenv('DB_PORT', 'Not set')}")
print(f"DB_NAME: {os.getenv('DB_NAME', 'Not set')}")
print(f"USE_SQLITE: {os.getenv('USE_SQLITE', 'Not set')}")

# Test database connection
try:
    from app import app, db
    with app.app_context():
        db.engine.execute("SELECT 1")
        print("✅ Database connection successful!")
except Exception as e:
    print(f"❌ Database connection failed: {e}")

print("\n=== Render Configuration Tips ===")
print("1. Make sure DATABASE_URL is set in Render environment variables")
print("2. Use format: postgresql://user:pass@host:5432/dbname")
print("3. Check if PostgreSQL is accessible from Render")
print("4. Verify FLASK_CONFIG=production")
