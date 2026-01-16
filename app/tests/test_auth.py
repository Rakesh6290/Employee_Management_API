def test_get_token(client):
    response = client.post("/api/auth/token")

    assert response.status_code == 200
    assert "access_token" in response.json()
