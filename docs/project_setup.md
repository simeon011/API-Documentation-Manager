# ⚙️ APILab Manager - Project Setup Guide

This guide provides step-by-step instructions on how to install, configure, and run the **APILab Manager** on your local machine. The project is optimized for a **PostgreSQL** environment and uses environment variables for secure configuration.

---

## 1. Prerequisites

Before you begin, ensure you have the following installed on your system:
* **Python 3.10+**: The core programming language.
* **PostgreSQL**: An active database server.
* **pip**: Python's package installer.
* **Git**: For cloning the repository.

---

## 2. Installation Steps

### Step 1: Clone the Repository
Open your terminal and clone the project to your local machine:
```bash
git clone <your-repository-url>
cd API_Documentation_Manager
```

### Step 2: Set Up a Virtual Environment
It is highly recommended to use a virtual environment to keep dependencies isolated.

 - #### Create the environment
```python -m venv venv```

 - #### Activate it (Windows)
```.\venv\Scripts\activate```

 - #### Activate it (Linux/macOS)
```source venv/bin/activate```

### Step 3: Install Dependencies
```pip install -r requirements.txt```

---

## 3. Environment Configuration (.env)
The project uses ```python-decouple``` to manage sensitive settings. You need to create a file named ```.env``` in the root directory (where ```manage.py``` is located) and fill in your credentials:
```
SECRET_KEY=your_secret_django_key
DEBUG=True

# Database Settings
DB_NAME=apilab_db
DB_USER=your_postgres_username
DB_PASSWORD=your_postgres_password
DB_HOST=127.0.0.1
DB_PORT=5432
```
---
## 4. Database Initialization

### Step 1: Create Database
Make sure you have created a database named ```apilab_db``` in your PostgreSQL server before proceeding.

### Step 2: Run Migrations

This will create the tables and automatically populate the database with our initial seed data (6 projects, 18+ endpoints, and tags).

```python manage.py migrate```

---

## 5. Running the Application
Start the Django development server with the following command:

```python manage.py runserver```  

You can now access the application at: http://127.0.0.1:8000/

---

## 🛠 Troubleshooting Common Issues
| Issue | Solution |
| :--- | :--- |
| **Database Connection Error** | Verify that PostgreSQL is running and the credentials in `.env` are correct. |
| **ModuleNotFoundError** | Ensure your virtual environment is active and run `pip install -r requirements.txt` again. |
| **Migrations Error** | Ensure the database named in `DB_NAME` actually exists in your PostgreSQL server. |
| **Static files (Icons) not loading** | Clear browser cache (Ctrl+F5) or check STATICFILES_DIRS in settings.py. |
| **Relation "projects_project" does not exist** | You skipped the python manage.py migrate step. | 

---

[Home](https://github.com/simeon011/API-Documentation-Manager/blob/main/README.md)
