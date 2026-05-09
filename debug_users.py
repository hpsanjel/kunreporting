#!/usr/bin/env python3
"""
Debug script to check users in the database
"""

from app import app, db, User
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def check_users():
    """Check all users in the database"""
    with app.app_context():
        try:
            users = User.query.all()
            print(f"Found {len(users)} users in database:")
            
            for user in users:
                print(f"\nUser ID: {user.id}")
                print(f"Username: '{user.username}'")
                print(f"Email: '{user.email}'")
                print(f"Full Name: '{user.full_name}'")
                print(f"Branch: '{user.branch}'")
                print(f"Is Admin: {user.is_admin}")
                print(f"Password Hash: {user.password_hash}")
                
                # Test password verification
                if user.username == 'admin':
                    print(f"Password check (admin123): {user.check_password('admin123')}")
                    print(f"Password check (wrong): {user.check_password('wrong')}")
                    
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    check_users()
