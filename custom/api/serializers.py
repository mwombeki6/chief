from rest_framework import serializers
from custom.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "employee_number",
            "title",
            "education_background",
            "student_reg_no",
            "class_course",
            "department",
            "gender",
            "is_institutionStaff",
            "is_institutionStudent",
        ]
