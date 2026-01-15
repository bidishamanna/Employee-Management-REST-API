from rest_framework import serializers
from employees.models import Employee

class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = "__all__"

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Name cannot be empty.")
        return value

    def validate_email(self, value):
        if not value:
            raise serializers.ValidationError("Email is required.")

        email = value.lower()

        # Case-insensitive uniqueness check
        queryset = Employee.objects.filter(email__iexact=email)

        # Exclude current instance during update
        if self.instance:
            queryset = queryset.exclude(pk=self.instance.pk)

        if queryset.exists():
            raise serializers.ValidationError(
                "Employee with this email already exists."
            )

        return email
