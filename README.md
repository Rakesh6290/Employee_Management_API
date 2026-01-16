# Employee Management API (FastAPI)

A secure and well-structured Employee Management REST API built using FastAPI.
The application supports JWT-based authentication, full CRUD operations for employees,
and automated test coverage using pytest.

This project was developed as part of a backend hiring assignment and follows
industry-standard best practices.

---

## Features

- JWT-based authentication
- Employee CRUD APIs
- Partial updates using PATCH
- Automated testing with pytest
- Interactive API documentation using Swagger and ReDoc
- Environment-based configuration

---

## Tech Stack

- Framework: FastAPI
- Language: Python 3.10+
- ORM: SQLAlchemy
- Database: SQLite (easily switchable)
- Authentication: OAuth2 with JWT
- Validation: Pydantic
- Testing: Pytest

---

## Project Structure

employee_api/
│
├── app/
│ ├── core/ # Application configuration and security
│ │ ├── config.py
│ │ └── security.py
│ │
│ ├── database.py # Database setup
│ │
│ ├── models/ # SQLAlchemy models
│ │ └── employee.py
│ │
│ ├── routes/ # API routes
│ │ ├── auth.py
│ │ └── employees.py
│ │
│ ├── schemas/ # Pydantic schemas
│ │ └── employee.py
│ │
│ ├── tests/ # Pytest test cases
│ │ ├── test_auth.py
│ │ └── test_employees.py
│ │
│ └── main.py # FastAPI application entry point
│
├── Dockerfile
├── requirements.txt
├── README.md
└── employees.db

yaml
Copy code

---

## Authentication Flow

1. User logs in via `/api/auth/token`
2. API returns a JWT access token
3. Token is passed in the `Authorization` header
4. Protected routes validate the token

Authorization: Bearer <access_token>

yaml
Copy code

---

## API Endpoints

### Authentication

| Method | Endpoint          | Description            |
|-------|-------------------|------------------------|
| POST  | `/api/auth/token` | Login and get JWT token |

### Employees

| Method | Endpoint              | Description        |
|-------|-----------------------|--------------------|
| POST  | `/api/employees/`     | Create employee    |
| GET   | `/api/employees/`     | List employees     |
| GET   | `/api/employees/{id}` | Get employee by ID |
| PATCH | `/api/employees/{id}` | Partial update     |
| PUT   | `/api/employees/{id}` | Full update        |
| DELETE| `/api/employees/{id}` | Delete employee    |

---

## Running the Project

### 1. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate
# Windows: venv\Scripts\activate
2. Install dependencies
bash
Copy code
pip install -r requirements.txt
3. Run the server
bash
Copy code
uvicorn app.main:app --reload
Swagger UI will be available at:

arduino
Copy code
http://127.0.0.1:8000/docs
Running Tests
bash
Copy code
pytest
All tests pass successfully.

Design Decisions
FastAPI chosen for high performance and automatic documentation

JWT used for stateless and secure authentication

PATCH and PUT used correctly for partial and full updates

Pytest ensures reliability and prevents regressions

Test Coverage
Authentication success and failure cases

Employee creation

Duplicate email validation

Not-found scenarios

Authorized access validation

Notes
SQLite is used for simplicity and demonstration purposes

The project can be easily extended to PostgreSQL or MySQL

Environment variables are managed using a .env file

Author
Jupally Rakesh
Backend Developer | Python | FastAPI
