from rest_framework import serializers
from staff.models import Staff
from custom.models import User


class StaffSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "employee_number",
            "title",
            "education_background",
            "department",
            "password",
            "password2",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
            "password2": {"write_only": True},
        }

    def save(self, **kwargs):
        user = User(
            username=self.validated_data["username"],
            first_name=self.validated_data["first_name"],
            last_name=self.validated_data["last_name"],
            email=self.validated_data["email"],
            employee_number=self.validated_data["employee_number"],
            title=self.validated_data["title"],
            education_background=self.validated_data["education_background"],
            department=self.validated_data["department"],
        )
        password = self.validated_data["password"]
        password2 = self.validated_data["password2"]

        if password != password2:
            raise serializers.ValidationError({"error": "password do not match"})
        user.set_password(password)
        user.is_institutionStaff = True
        user.save()
        Staff.objects.create(user=user)

        return user

class UpdateSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=False, allow_null=True)
    last_name = serializers.CharField(required=False, allow_null=True)
    username = serializers.CharField(required=False,allow_null=True)
    email = serializers.EmailField(required=False,allow_null=True)
    employee_number = serializers.CharField(allow_null=True)
    title = serializers.CharField(allow_null=True)
    education_background = serializers.CharField(allow_null=True)
    department = serializers.CharField(allow_null=True)

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "employee_number",
            "title",
            "education_background",
            "department",
        )