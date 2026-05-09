# Company Report System

A comprehensive project and grant management system for Norwegian companies with branches in Oslo and Bergen.

## Features

### 🔐 User Management
- Role-based access control (Administrator/Staff)
- Branch-specific user assignments (Oslo/Bergen)
- Secure authentication system

### 📊 Project Management
- Add, edit, and delete projects
- Branch-based project organization
- Detailed project descriptions

### 💰 Grant Application Tracking
- Track grant applications with status management
- Applied/Granted/Rejected status tracking
- Financial amount tracking in NOK

### 📝 Introduction Section
- Admin-only editable introduction
- Appears in all generated reports

### 🔍 Audit Trail
- Complete change tracking
- Records who changed what and when
- Admin-only access to audit logs

### 📄 Report Generation
- PDF report export
- Word document export
- Professional formatting

## Installation

### Prerequisites
- Python 3.8+
- pip package manager
- PostgreSQL 12+ (or Docker for containerized setup)

### Setup Instructions

#### Option 1: Using Docker (Recommended)
1. **Clone or download the project files**

2. **Start PostgreSQL and application:**
   ```bash
   docker-compose up -d
   ```

3. **Access the application:**
   - Open your web browser
   - Navigate to `http://localhost:5001`

#### Option 2: Manual PostgreSQL Setup
1. **Install PostgreSQL** on your system

2. **Clone or download the project files**

3. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   ```bash
   cp .env.example .env
   # Edit .env with your PostgreSQL credentials
   ```

5. **Create database and tables:**
   ```bash
   python3 setup_database.py
   ```

6. **Run the application:**
   ```bash
   python3 app.py
   ```

7. **Access the application:**
   - Open your web browser
   - Navigate to `http://localhost:5001`

### Default Admin Account
- **Username:** `admin`
- **Password:** `admin123`

⚠️ **Important:** Change the default admin password after first login!

### Environment Variables
Create a `.env` file based on `.env.example`:
```bash
# Flask Configuration
FLASK_CONFIG=development
SECRET_KEY=your-secret-key-change-in-production

# PostgreSQL Database Configuration
DATABASE_URL=postgresql://username:password@localhost:5432/company_reports

# Or use individual database parameters
DB_USER=postgres
DB_PASSWORD=password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=company_reports
```

## User Management

### Creating New Users
Use the included user management script:

```bash
python user_management.py
```

This script provides options to:
- Create new user accounts
- List all users
- Delete user accounts
- Reset passwords

### User Roles
- **Administrator:** Full access to all features including audit logs and introduction editing
- **Staff:** Can manage projects and grant applications

## Branch Structure

The system supports two branches:
- **Oslo**
- **Bergen**

Users are assigned to specific branches, and projects/grant applications are categorized by branch.

## Report Generation

### PDF Reports
- Professional formatting
- Includes all sections: Introduction, Projects, Grant Applications
- Automatic pagination

### Word Documents
- .docx format
- Editable after generation
- Structured with headings and formatting

## Security Features

- Password hashing using Werkzeug
- Session-based authentication
- Role-based access control
- Audit trail for all changes

## Database

The system uses SQLite database (`company_reports.db`) which includes:
- Users table
- Projects table
- Grant applications table
- Introduction table
- Audit log table

## File Structure

```
windsurf-project/
├── app.py                 # Main Flask application
├── user_management.py     # User management utility
├── requirements.txt       # Python dependencies
├── company_reports.db    # SQLite database (auto-created)
├── templates/            # HTML templates
│   ├── base.html
│   ├── login.html
│   ├── dashboard.html
│   ├── introduction.html
│   ├── projects.html
│   ├── add_project.html
│   ├── edit_project.html
│   ├── grants.html
│   ├── add_grant.html
│   ├── edit_grant.html
│   └── audit.html
└── README.md             # This file
```

## Usage Guide

### For Administrators
1. Log in with admin credentials
2. Create user accounts for staff members
3. Edit the introduction section
4. Monitor audit logs
5. Generate reports as needed

### For Staff Members
1. Log in with assigned credentials
2. Add and manage projects
3. Track grant applications
4. Update project information
5. Generate reports

## Support

For technical support or questions about the system:
1. Check the audit logs for change history
2. Review user permissions if access issues occur
3. Ensure all dependencies are properly installed

## Development

The system is built with:
- **Flask** - Web framework
- **Flask-SQLAlchemy** - Database ORM
- **Flask-Login** - Authentication
- **Bootstrap** - UI framework
- **python-docx** - Word document generation
- **ReportLab** - PDF generation

## License

This project is proprietary and intended for internal company use only.
