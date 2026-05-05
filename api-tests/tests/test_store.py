import pytest


ORDER_PAYLOAD = {
    "id": 987654321,
    "petId": 123456789,
    "quantity": 1,
    "status": "placed",
    "complete": False,
}


class TestStore:
    def test_get_inventory(self, client):
        response = client.get("/store/inventory")
        assert response.status_code == 200
        assert isinstance(response.json(), dict)

    def test_place_order(self, client):
        response = client.post("/store/order", json=ORDER_PAYLOAD)
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == ORDER_PAYLOAD["id"]
        assert data["status"] == "placed"

    def test_get_order_by_id(self, client):
        response = client.get(f"/store/order/{ORDER_PAYLOAD['id']}")
        assert response.status_code == 200
        assert response.json()["id"] == ORDER_PAYLOAD["id"]

    def test_get_order_not_found(self, client):
        response = client.get("/store/order/999999999")
        assert response.status_code == 404

    def test_delete_order(self, client):
        response = client.delete(f"/store/order/{ORDER_PAYLOAD['id']}")
        assert response.status_code == 200

    def test_delete_order_not_found(self, client):
        response = client.delete("/store/order/999999999")
        assert response.status_code == 404
