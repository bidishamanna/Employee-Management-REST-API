Employee Management REST API
 Project Overview

This project is a secure RESTful API built using Django REST Framework to manage employees in a company.
It supports CRUD operations, JWT authentication, validation, filtering, pagination, and unit testing, following REST best practices.
This project was developed as part of a Python Backend Developer Hiring Assignment.

Features

JWT-based authentication (SimpleJWT)
Secure employee CRUD operations
Email and name validation
Filtering by department and role
Pagination (10 records per page)
Proper HTTP status codes
Unit tests for all endpoints
PostgreSQL database support

Technology Stack

Python 3.x
Django REST Framework
PostgreSQL
JWT Authentication (SimpleJWT)
Postman (API Testing)

🔐 Authentication

JWT (JSON Web Token) authentication is implemented using djangorestframework-simplejwt.
All employee endpoints are protected and require a valid access token.

🔑 Obtain Token
POST /api/token/

Request Body
{
  "username": "your_username",
  "password": "your_password"
}
Response
{
  "refresh": "refresh_token",
  "access": "access_token"
}


Use the access token in Postman:

Authorization → Bearer Token → <access_token>

📚 API Endpoints
Method	Endpoint	Description
POST	/api/token/	Obtain JWT token
POST	/api/employees/	Create employee
GET	/api/employees/	List employees
GET	/api/employees/{id}/	Retrieve employee
PUT	/api/employees/{id}/	Update employee
DELETE	/api/employees/{id}/	Delete employee
🧾 Employee Model
Field	Description
id	Auto-generated primary key
name	Required string
email	Required, unique, valid email
department	Optional
role	Optional
date_joined	Auto-generated
✅ Validation Rules

Name cannot be empty
Email must be valid and unique
Duplicate email → 400 Bad Request
Invalid ID → 404 Not Found

⚠️ HTTP Status Codes
Code	Meaning
201	Created
400	Bad Request
404	Not Found
204	No Content
🔍 Filtering

Filter employees using query parameters:

GET /api/employees/?department=HR
GET /api/employees/?role=Manager

📄 Pagination
Pagination is enabled globally:
Page size: 10 records
GET /api/employees/?page=2

🧪 Testing
Unit tests are written using APITestCase and cover:
Authentication
Employee creation
Duplicate email validation
Retrieval errors (404)
Deletion
Protected endpoint access

Run tests:
python manage.py test employees

▶️ Run Project Locally
1️⃣ Clone repository
git clone <repository-url>
cd employee_api

2️⃣ Create virtual environment
python -m venv myenv
myenv\Scripts\activate   # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Configure PostgreSQL

Update settings.py with database credentials.

5️⃣ Apply migrations
python manage.py makemigrations
python manage.py migrate

6️⃣ Create superuser
python manage.py createsuperuser

7️⃣ Run server
python manage.py runserver

📬 Postman Testing
JWT Login
Employee CRUD
Filtering & Pagination
Error handling

(Postman screenshots and collection are attached in documentation.)
