# Employee Management API (FastAPI)

A secure, well-structured **Employee Management REST API** built using **FastAPI**, featuring **JWT-based authentication**, **CRUD operations**, and **pytest-based test coverage**.

This project was developed as part of a backend hiring assignment and follows industry-standard best practices.

---

## 🚀 Features

* 🔐 JWT Authentication (Token-based)
* 👤 Employee CRUD APIs
* ✏️ Partial updates using PATCH
* 🧪 Automated testing with pytest
* 📄 Interactive API docs (Swagger & ReDoc)
* ⚙️ Environment-based configuration

---

## 🛠 Tech Stack

* **Framework:** FastAPI
* **Language:** Python 3.10+
* **ORM:** SQLAlchemy
* **Database:** SQLite (easily switchable)
* **Auth:** OAuth2 + JWT
* **Validation:** Pydantic
* **Testing:** Pytest

---

## 📂 Project Structure

```
employee_api/
│
├── app/
│ ├── core/ # App configuration & security
│ │ ├── config.py
│ │ └── security.py
│ │
│ ├── database/ # Database setup
│ │ └── session.py
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
│ └── main.py # FastAPI app entry point
│
├── Dockerfile
├── requirements.txt
└── README.md
├── employees.db

```

---

## 🔑 Authentication Flow

1. User logs in via `/api/auth/token`
2. API returns a JWT access token
3. Token is passed in the `Authorization` header
4. Protected routes validate the token

```
Authorization: Bearer <access_token>
```

---

## 📌 API Endpoints

### Auth

| Method | Endpoint          | Description       |
| ------ | ----------------- | ----------------- |
| POST   | `/api/auth/token` | Login & get token |

### Employees

| Method | Endpoint              | Description     |
| ------ | --------------------- | --------------- |
| POST   | `/api/employees/`     | Create employee |
| GET    | `/api/employees/`     | List employees  |
| GET    | `/api/employees/{id}` | Get employee    |
| PATCH  | `/api/employees/{id}` | Partial update  |
| PUT    | `/api/employees/{id}` | Full update     |
| DELETE | `/api/employees/{id}` | Delete employee |

---

## ▶️ Running the Project

### 1️⃣ Create virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the server

```bash
uvicorn app.main:app --reload
```

Access Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## 🧪 Running Tests

```bash
pytest
```

✔ All tests pass successfully

---

## 🧠 Design Decisions

* **FastAPI** chosen for async performance & automatic docs
* **JWT** for stateless authentication
* **PATCH vs PUT** used correctly for partial vs full updates
* **Pytest** ensures reliability & prevents regressions

---

## ✅ Test Coverage

* Authentication success & failure
* Employee creation
* Duplicate email validation
* Not-found scenarios
* Authorized access validation

---

## 📌 Notes

* SQLite used for simplicity
* Easily extendable to PostgreSQL/MySQL
* Environment variables managed via `.env`

---

## 👤 Author

**Jupally Rakesh**
Backend Developer | Python | FastAPI

---


