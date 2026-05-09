#!/usr/bin/env python3
"""
Database setup script for PostgreSQL
This script creates the database and initial admin user for PostgreSQL.
"""

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from app import app, db, User
import os

def create_database():
    """Create the PostgreSQL database if it doesn't exist"""
    db_name = os.getenv('DB_NAME', 'company_reports')
    db_user = os.getenv('DB_USER', 'postgres')
    db_password = os.getenv('DB_PASSWORD', 'password')
    db_host = os.getenv('DB_HOST', 'localhost')
    db_port = os.getenv('DB_PORT', '5432')
    
    try:
        # Connect to PostgreSQL server (without specifying database)
        conn = psycopg2.connect(
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port
        )
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = conn.cursor()
        
        # Check if database exists
        cursor.execute(f"SELECT 1 FROM pg_catalog.pg_database WHERE datname = '{db_name}'")
        exists = cursor.fetchone()
        
        if not exists:
            # Create database
            cursor.execute(f'CREATE DATABASE {db_name}')
            print(f"✅ Database '{db_name}' created successfully!")
        else:
            print(f"ℹ️  Database '{db_name}' already exists!")
        
        cursor.close()
        conn.close()
        
    except Exception as e:
        print(f"❌ Error creating database: {e}")
        return False
    
    return True

def create_tables_and_admin():
    """Create tables and initial admin user"""
    with app.app_context():
        try:
            # Create all tables
            db.create_all()
            print("✅ Database tables created successfully!")
            
            # Create admin user if not exists
            admin = User.query.filter_by(username='admin').first()
            if not admin:
                admin = User(
                    username='admin',
                    email='admin@company.no',
                    full_name='System Administrator',
                    branch='Oslo',
                    is_admin=True
                )
                admin.set_password('admin123')
                db.session.add(admin)
                db.session.commit()
                print("✅ Admin user created: username='admin', password='admin123'")
            else:
                print("ℹ️  Admin user already exists!")
                
        except Exception as e:
            print(f"❌ Error setting up database: {e}")
            return False
    
    return True

def main():
    """Main setup function"""
    print("🚀 Setting up PostgreSQL database for Company Report System")
    print("=" * 60)
    
    # Load environment variables
    from dotenv import load_dotenv
    load_dotenv()
    
    # Create database
    if not create_database():
        print("❌ Database setup failed!")
        return
    
    # Create tables and admin user
    if not create_tables_and_admin():
        print("❌ Tables and admin setup failed!")
        return
    
    print("\n🎉 Database setup completed successfully!")
    print("\n📋 Next steps:")
    print("1. Start the application: python3 app.py")
    print("2. Login with: username='admin', password='admin123'")
    print("3. Change the default admin password!")

if __name__ == "__main__":
    main()
