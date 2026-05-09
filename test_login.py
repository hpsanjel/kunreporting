#!/usr/bin/env python3
"""
Test login for specific user
"""

from app import app, db, User
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_user_login():
    """Test login for the jayasanjel user"""
    with app.app_context():
        try:
            user = User.query.filter_by(username='jayasanjel').first()
            if user:
                print(f"User found: {user.username}")
                print(f"Email: {user.email}")
                print(f"Full Name: {user.full_name}")
                
                # Test with different passwords
                test_passwords = ['admin123', 'password', 'jayasanjel', '', '123456']
                for pwd in test_passwords:
                    result = user.check_password(pwd)
                    print(f"Password '{pwd}': {result}")
            else:
                print("User 'jayasanjel' not found!")
                
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    test_user_login()
