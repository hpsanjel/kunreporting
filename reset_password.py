#!/usr/bin/env python3
"""
Reset password for a specific user
"""

from app import app, db, User
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def reset_user_password():
    """Reset password for jayasanjel user"""
    with app.app_context():
        try:
            user = User.query.filter_by(username='jayasanjel').first()
            if user:
                # Reset password to 'jayasanjel123'
                user.set_password('jayasanjel123')
                db.session.commit()
                print(f"✅ Password reset for user '{user.username}'")
                print(f"📧 Email: {user.email}")
                print(f"👤 Full Name: {user.full_name}")
                print(f"🔑 New Password: jayasanjel123")
                print("\n⚠️  Please change this password after logging in!")
                
                # Test the new password
                if user.check_password('jayasanjel123'):
                    print("✅ Password verification successful!")
                else:
                    print("❌ Password verification failed!")
            else:
                print("❌ User 'jayasanjel' not found!")
                
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    reset_user_password()
