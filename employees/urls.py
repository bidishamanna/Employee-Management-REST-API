from django.urls import path
from employees.views import EmployeeListCreateView, EmployeeDetailView

urlpatterns = [
    path("employees/", EmployeeListCreateView.as_view()),
    path("employees/<int:pk>/", EmployeeDetailView.as_view()),
]
