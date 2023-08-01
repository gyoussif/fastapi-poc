import unittest

from fastapi.testclient import TestClient

from src.main import app


class TestCartAPI(unittest.TestCase):

    def setUp(self):
        self.client = TestClient(app)

    def test_list_carts(self):
        response = self.client.get("/api/v1/cart/")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_get_cart_details(self):
        response = self.client.get("/api/v1/cart/1/")
        self.assertEqual(response.status_code, 200)
        # self.assertIn("id", response.json())

    def test_get_customer_carts(self):
        response = self.client.get("/api/v1/cart/customer/1/")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_create_cart(self):
        cart_data = {"is_guest": False, "customer_id": 1}
        response = self.client.post("/api/v1/cart/", json=cart_data)
        self.assertEqual(response.status_code, 200)
        # self.assertIn("id", response.json())

    def test_update_cart_not_found(self):
        cart_data = {"is_guest": False, "customer_id": 1}
        response = self.client.put("/api/v1/cart/1/", json=cart_data)
        self.assertEqual(response.status_code, 404)
        # self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.json()["name"], "Updated Cart")

    def test_delete_cart(self):
        response = self.client.delete("/api/v1/cart/1/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["ok"], True)
