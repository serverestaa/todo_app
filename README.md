# TodoApp - FastAPI Project

TodoApp is a simple task management application built with **FastAPI**, **SQLAlchemy**, **Jinja2**, and **PostgreSQL**. This app allows users to register, log in, create, edit, and delete tasks (todos), with additional administrative features for managing tasks.

## Features

- User registration and login with JWT-based authentication.
- Create, edit, and delete tasks (todos).
- Task management interface with priorities and completion status.
- Administrative capabilities for managing tasks by all users.
- RESTful API for interacting with todos and users.
- Secure password hashing using bcrypt.
- Fully functional front-end using Jinja2 templates and Bootstrap for styling.
- Basic unit tests for authentication, task management, and user roles.

## Project Structure
```
.
├── __init__.py
├── alembic
│   ├── README
│   ├── env.py
│   ├── script.py.mako
│   └── versions
├── alembic.ini
├── database.py
├── main.py
├── models.py
├── routers
│   ├── __init__.py
│   ├── admin.py
│   ├── auth.py
│   ├── todos.py
│   └── users.py
├── static
│   ├── css
│   │   ├── base.css
│   │   └── bootstrap.css
│   └── js
│       ├── base.js
│       ├── bootstrap.js
│       ├── bootstrap.js.map
│       ├── jquery-slim.js
│       ├── popper.js
│       └── popper.min.js.map
├── templates
│   ├── add-todo.html
│   ├── edit-todo.html
│   ├── home.html
│   ├── layout.html
│   ├── login.html
│   ├── navbar.html
│   ├── register.html
│   └── todo.html
├── test
│   ├── __init__.py
│   ├── test_admin.py
│   ├── test_auth.py
│   ├── test_example.py
│   ├── test_main.py
│   ├── test_todos.py
│   ├── test_users.py
│   └── utils.py
└── test_main.http
```
## Getting Started

### Prerequisites

To run this project locally, you need:

- Python 3.8+
- PostgreSQL
- Virtual environment (recommended)

### Installation

1. Clone the repository**:
   ```
   bash
   git clone https://github.com/yourusername/todoapp.git
   cd todoapp
   ```
2.	Create and activate a virtual environment: 
   ```
   python -m venv venv
   source venv/bin/activate
   ```
3.	Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4.	Set up environment variables:
Create a .env file in the root of your project and add the following:
   ```
   SECRET=your_jwt_secret
   ALGORITHM=HS256
   BCRYPT_SCHEMES=bcrypt
   db_password=your_postgresql_password
   ```
5.	Set up the database:
•	Create a PostgreSQL database.
•	Modify the connection string in database.py to match your database credentials:
   ```
   SQLALCHEMY_DATABASE_URL = "postgresql://username:password@localhost/todoapp_db"
   ```
6.	Run database migrations:
   ```
   alembic upgrade head
   ```
8.	Run the application:
   ```
   uvicorn main:app --reload
   ```

Running Tests

To run the tests, use the following command:
   ```
   pytest
   ```
API Endpoints

Here are some key API endpoints:

Authentication

	•	POST /auth/token: Obtain JWT token.
	•	POST /auth/register: Register a new user.

Todos

	•	GET /todos/todo: Get all todos (requires authentication).
	•	POST /todos/todo: Create a new todo (requires authentication).
	•	PUT /todos/todo/{todo_id}: Update a todo (requires authentication).
	•	DELETE /todos/todo/{todo_id}: Delete a todo (requires authentication).

Admin (only for users with admin role)

	•	GET /admin/todo: Get all todos (requires admin role).
	•	DELETE /admin/todo/{todo_id}: Delete any user’s todo (requires admin role).

Frontend

The frontend is built using Jinja2 templates and Bootstrap 4.3.1 for styling.

Pages

	•	Home Page: Welcome page.
	•	Todo List Page: List of todos with options to edit or mark as complete.
	•	Add Todo Page: Form to add a new todo.
	•	Edit Todo Page: Form to edit an existing todo.
	•	Login Page: Form to log in.
	•	Register Page: Form to register a new account.

Technologies Used

	•	FastAPI: Backend framework
	•	SQLAlchemy: ORM for database interactions
	•	PostgreSQL: Relational database
	•	Jinja2: Templating engine for HTML
	•	Bootstrap: Frontend framework
	•	Passlib: For secure password hashing
	•	Pytest: For unit testing
