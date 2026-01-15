from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

class EmployeeAPITest(APITestCase):

    def setUp(self):
        # Create a system user
        self.user = User.objects.create_user(username="testuser", password="test123")

        # Generate JWT token for this user
        refresh = RefreshToken.for_user(self.user)
        self.access_token = str(refresh.access_token)

        # Set token in Authorization header
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.access_token}")

    # Helper method to create employee
    def create_employee(self, name="John Doe", email="john@example.com", department="HR", role="Manager"):
        data = {
            "name": name,
            "email": email,
            "department": department,
            "role": role
        }
        return self.client.post("/api/employees/", data, format="json")

    # Test creating an employee
    def test_create_employee(self):
        response = self.create_employee()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["name"], "John Doe")
        self.assertEqual(response.data["email"], "john@example.com")

    # Test duplicate email
    def test_duplicate_email(self):
        self.create_employee()
        response = self.create_employee(name="Jane Doe")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # Test retrieving non-existent employee
    def test_get_employee_not_found(self):
        response = self.client.get("/api/employees/999/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    # Test updating employee
    def test_update_employee(self):
        response = self.create_employee()
        emp_id = response.data["id"]

        update_data = {
            "name": "John Updated",
            "email": "john@example.com",
            "department": "Engineering",
            "role": "Lead"
        }
        update_response = self.client.put(f"/api/employees/{emp_id}/", update_data, format="json")
        self.assertEqual(update_response.status_code, status.HTTP_200_OK)
        self.assertEqual(update_response.data["name"], "John Updated")
        self.assertEqual(update_response.data["department"], "Engineering")

    # Test deleting employee
    def test_delete_employee(self):
        response = self.create_employee(name="Delete Me", email="delete@example.com")
        emp_id = response.data["id"]

        delete_response = self.client.delete(f"/api/employees/{emp_id}/")
        self.assertEqual(delete_response.status_code, status.HTTP_204_NO_CONTENT)

        # Verify deletion
        get_response = self.client.get(f"/api/employees/{emp_id}/")
        self.assertEqual(get_response.status_code, status.HTTP_404_NOT_FOUND)

    # Test filtering by department and role
    def test_filtering(self):
        self.create_employee(name="HR Person", email="hr@example.com", department="HR", role="Manager")
        self.create_employee(name="Eng Person", email="eng@example.com", department="Engineering", role="Developer")

        # Filter by department
        response = self.client.get("/api/employees/?department=HR")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)
        self.assertEqual(response.data["results"][0]["department"], "HR")

        # Filter by role
        response = self.client.get("/api/employees/?role=Developer")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)
        self.assertEqual(response.data["results"][0]["role"], "Developer")

    # Test pagination (PAGE_SIZE = 10)
    def test_pagination(self):
        for i in range(15):
            self.create_employee(name=f"Emp{i}", email=f"emp{i}@example.com")

        response = self.client.get("/api/employees/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 10)  # page size = 10
        self.assertIn("next", response.data)
        self.assertIn("previous", response.data)
