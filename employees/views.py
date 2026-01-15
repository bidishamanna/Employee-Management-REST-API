from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from employees.models import Employee
from employees.serializers import EmployeeSerializer

class EmployeeListCreateView(generics.ListCreateAPIView):
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Employee.objects.all().order_by("id")

        department = self.request.query_params.get("department")
        role = self.request.query_params.get("role")

        if department:
            queryset = queryset.filter(department=department)
        if role:
            queryset = queryset.filter(role=role)

        return queryset


class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]








# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status, permissions
# from .models import Employee
# from employees.serializers import EmployeeSerializer


# class EmployeeListCreateView(APIView):
#     permission_classes = [permissions.IsAuthenticated]

#     def get(self, request):
#         queryset = Employee.objects.all().order_by("id")

#         department = request.query_params.get("department")
#         role = request.query_params.get("role")

#         if department:
#             queryset = queryset.filter(department=department)
#         if role:
#             queryset = queryset.filter(role=role)

#         serializer = EmployeeSerializer(queryset, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def post(self, request):
#         serializer = EmployeeSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# class EmployeeDetailView(APIView):
#     permission_classes = [permissions.IsAuthenticated]

#     def get_object(self, pk):
#         try:
#             return Employee.objects.get(pk=pk)
#         except Employee.DoesNotExist:
#             return None

#     def get(self, request, pk):
#         employee = self.get_object(pk)
#         if not employee:
#             return Response(
#                 {"detail": "Employee not found"},
#                 status=status.HTTP_404_NOT_FOUND
#             )

#         serializer = EmployeeSerializer(employee)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def put(self, request, pk):
#         employee = self.get_object(pk)
#         if not employee:
#             return Response(
#                 {"detail": "Employee not found"},
#                 status=status.HTTP_404_NOT_FOUND
#             )

#         serializer = EmployeeSerializer(employee, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         employee = self.get_object(pk)
#         if not employee:
#             return Response(
#                 {"detail": "Employee not found"},
#                 status=status.HTTP_404_NOT_FOUND
#             )

#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


