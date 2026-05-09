#!/usr/bin/env python3
"""
User Management Script for Company Report System
This script helps administrators create and manage user accounts for Oslo and Bergen branches.
"""

from app import app, db, User
from werkzeug.security import generate_password_hash
import getpass
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def create_user():
    """Create a new user account"""
    print("\n=== Create New User ===")
    
    username = input("Enter username: ").strip()
    if not username:
        print("Username cannot be empty!")
        return
    
    # Check if username already exists
    with app.app_context():
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            print(f"Username '{username}' already exists!")
            return
    
    email = input("Enter email: ").strip()
    if not email:
        print("Email cannot be empty!")
        return
    
    full_name = input("Enter full name: ").strip()
    if not full_name:
        print("Full name cannot be empty!")
        return
    
    print("\nAvailable branches:")
    print("1. Oslo")
    print("2. Bergen")
    
    branch_choice = input("Select branch (1 or 2): ").strip()
    if branch_choice == "1":
        branch = "Oslo"
    elif branch_choice == "2":
        branch = "Bergen"
    else:
        print("Invalid branch choice!")
        return
    
    admin_choice = input("Is this user an administrator? (y/n): ").strip().lower()
    is_admin = admin_choice in ['y', 'yes']
    
    password = getpass.getpass("Enter password: ")
    if not password:
        print("Password cannot be empty!")
        return
    
    confirm_password = getpass.getpass("Confirm password: ")
    if password != confirm_password:
        print("Passwords do not match!")
        return
    
    # Create user
    with app.app_context():
        user = User(
            username=username,
            email=email,
            full_name=full_name,
            branch=branch,
            is_admin=is_admin
        )
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        
        print(f"\n✅ User '{username}' created successfully!")
        print(f"   Name: {full_name}")
        print(f"   Email: {email}")
        print(f"   Branch: {branch}")
        print(f"   Role: {'Administrator' if is_admin else 'Staff'}")

def list_users():
    """List all users in the system"""
    print("\n=== All Users ===")
    
    with app.app_context():
        users = User.query.order_by(User.branch, User.full_name).all()
        
        if not users:
            print("No users found in the system.")
            return
        
        print(f"{'Username':<15} {'Full Name':<25} {'Email':<30} {'Branch':<8} {'Role':<12}")
        print("-" * 95)
        
        for user in users:
            role = "Admin" if user.is_admin else "Staff"
            print(f"{user.username:<15} {user.full_name:<25} {user.email:<30} {user.branch:<8} {role:<12}")

def delete_user():
    """Delete a user account"""
    print("\n=== Delete User ===")
    
    username = input("Enter username to delete: ").strip()
    if not username:
        print("Username cannot be empty!")
        return
    
    with app.app_context():
        user = User.query.filter_by(username=username).first()
        if not user:
            print(f"User '{username}' not found!")
            return
        
        if user.username == "admin":
            print("Cannot delete the default admin user!")
            return
        
        print(f"\nUser found:")
        print(f"  Name: {user.full_name}")
        print(f"  Email: {user.email}")
        print(f"  Branch: {user.branch}")
        print(f"  Role: {'Administrator' if user.is_admin else 'Staff'}")
        
        confirm = input(f"\nAre you sure you want to delete user '{username}'? (y/n): ").strip().lower()
        if confirm in ['y', 'yes']:
            db.session.delete(user)
            db.session.commit()
            print(f"✅ User '{username}' deleted successfully!")
        else:
            print("Deletion cancelled.")

def reset_password():
    """Reset user password"""
    print("\n=== Reset Password ===")
    
    username = input("Enter username: ").strip()
    if not username:
        print("Username cannot be empty!")
        return
    
    with app.app_context():
        user = User.query.filter_by(username=username).first()
        if not user:
            print(f"User '{username}' not found!")
            return
        
        print(f"\nUser found: {user.full_name} ({user.branch})")
        
        new_password = getpass.getpass("Enter new password: ")
        if not new_password:
            print("Password cannot be empty!")
            return
        
        confirm_password = getpass.getpass("Confirm new password: ")
        if new_password != confirm_password:
            print("Passwords do not match!")
            return
        
        user.set_password(new_password)
        db.session.commit()
        print(f"✅ Password for '{username}' reset successfully!")

def main():
    """Main menu"""
    print("Company Report System - User Management")
    print("=" * 50)
    
    while True:
        print("\nMenu:")
        print("1. Create new user")
        print("2. List all users")
        print("3. Delete user")
        print("4. Reset password")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == "1":
            create_user()
        elif choice == "2":
            list_users()
        elif choice == "3":
            delete_user()
        elif choice == "4":
            reset_password()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
