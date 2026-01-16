import uuid

def get_auth_header(client):
    token_response = client.post("/api/auth/token")
    token = token_response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}




def test_create_employee(client):
    headers = get_auth_header(client)

    payload = {
        "name": "John Doe",
        "email": f"john_{uuid.uuid4()}@example.com",
        "department": "Engineering",
        "role": "Developer"
    }

    response = client.post("/api/employees/", json=payload, headers=headers)

    assert response.status_code == 201


def test_duplicate_email(client):
    headers = get_auth_header(client)

    payload = {
        "name": "Jane",
        "email": "duplicate@example.com",
        "department": "HR",
        "role": "Manager"
    }

    client.post("/api/employees/", json=payload, headers=headers)
    response = client.post("/api/employees/", json=payload, headers=headers)

    assert response.status_code == 400



def test_get_employee_not_found(client):
    headers = get_auth_header(client)

    response = client.get("/api/employees/9999", headers=headers)

    assert response.status_code == 404


def test_unauthorized_access(client):
    response = client.get("/api/employees/")
    assert response.status_code == 403 or response.status_code == 401
