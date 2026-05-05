import pytest


PET_PAYLOAD = {
    "id": 123456789,
    "name": "Buddy",
    "status": "available",
    "category": {"id": 1, "name": "Dogs"},
    "photoUrls": ["https://example.com/buddy.jpg"],
    "tags": [{"id": 1, "name": "friendly"}],
}


class TestPet:
    def test_create_pet(self, client):
        response = client.post("/pet", json=PET_PAYLOAD)
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == PET_PAYLOAD["id"]
        assert data["name"] == PET_PAYLOAD["name"]

    def test_get_pet_by_id(self, client):
        response = client.get(f"/pet/{PET_PAYLOAD['id']}")
        assert response.status_code == 200
        assert response.json()["id"] == PET_PAYLOAD["id"]

    def test_update_pet(self, client):
        updated = {**PET_PAYLOAD, "name": "Buddy Updated", "status": "pending"}
        response = client.put("/pet", json=updated)
        assert response.status_code == 200
        assert response.json()["name"] == "Buddy Updated"
        assert response.json()["status"] == "pending"

    def test_find_pets_by_status(self, client):
        for status in ["available", "pending", "sold"]:
            response = client.get("/pet/findByStatus", params={"status": status})
            assert response.status_code == 200
            assert isinstance(response.json(), list)

    def test_update_pet_via_form(self, client):
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        data = {"name": "Buddy Form", "status": "sold"}
        response = client.post(f"/pet/{PET_PAYLOAD['id']}", data=data, headers=headers)
        assert response.status_code == 200

    @pytest.mark.xfail(
        reason="uploadFile endpoint retorna 404 no servidor público petstore.swagger.io/v2 "
               "independente do pet existir — limitação conhecida da API demo.",
        strict=False,
    )
    def test_upload_pet_image(self, client):
        files = {"file": ("test.jpg", b"fake-image-data", "image/jpeg")}
        # Content-Type: None removes the session default so requests sets multipart boundary
        response = client.post(
            f"/pet/{PET_PAYLOAD['id']}/uploadFile",
            files=files,
            headers={"Content-Type": None},
        )
        assert response.status_code == 200

    def test_delete_pet(self, client):
        response = client.delete(f"/pet/{PET_PAYLOAD['id']}")
        assert response.status_code == 200

    def test_get_pet_not_found(self, client):
        response = client.get("/pet/999999999999")
        assert response.status_code == 404

   
