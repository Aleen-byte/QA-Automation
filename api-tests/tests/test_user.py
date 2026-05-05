import pytest


USER_PAYLOAD = {
    "id": 111222333,
    "username": "test_user_qa",
    "firstName": "Test",
    "lastName": "User",
    "email": "testuser@qa.com",
    "password": "senha123",
    "phone": "11999999999",
    "userStatus": 1,
}


class TestUser:
    def test_create_user(self, client):
        response = client.post("/user", json=USER_PAYLOAD)
        assert response.status_code == 200

    def test_create_users_with_list(self, client):
        users = [
            {**USER_PAYLOAD, "id": 111222334, "username": "list_user_1"},
            {**USER_PAYLOAD, "id": 111222335, "username": "list_user_2"},
        ]
        response = client.post("/user/createWithList", json=users)
        assert response.status_code == 200

    def test_create_users_with_array(self, client):
        users = [{**USER_PAYLOAD, "id": 111222336, "username": "array_user_1"}]
        response = client.post("/user/createWithArray", json=users)
        assert response.status_code == 200

    def test_get_user_by_username(self, client):
        response = client.get(f"/user/{USER_PAYLOAD['username']}")
        assert response.status_code == 200
        assert response.json()["username"] == USER_PAYLOAD["username"]

    def test_update_user(self, client):
        updated = {**USER_PAYLOAD, "firstName": "Updated"}
        response = client.put(f"/user/{USER_PAYLOAD['username']}", json=updated)
        assert response.status_code == 200

    def test_login(self, client):
        params = {"username": USER_PAYLOAD["username"], "password": USER_PAYLOAD["password"]}
        response = client.get("/user/login", params=params)
        assert response.status_code == 200
        assert "logged in" in response.json().get("message", "").lower()

    def test_logout(self, client):
        response = client.get("/user/logout")
        assert response.status_code == 200

    def test_get_user_not_found(self, client):
        response = client.get("/user/usuario_que_nao_existe_xyz")
        assert response.status_code == 404

    def test_delete_user(self, client):
        response = client.delete(f"/user/{USER_PAYLOAD['username']}")
        assert response.status_code == 200
