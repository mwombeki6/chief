from rest_framework import serializers
from student.models import Student
from custom.models import User


class StudentSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "student_reg_no",
            "class_course",
            "department",
            "password",
            "password2",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def save(self, **kwargs):
        user = User(
            username=self.validated_data["username"],
            first_name=self.validated_data["first_name"],
            last_name=self.validated_data["last_name"],
            email=self.validated_data["email"],
            student_reg_no=self.validated_data["student_reg_no"],
            class_course=self.validated_data["class_course"],
            department=self.validated_data["department"],
        )
        password = self.validated_data["password"]
        password2 = self.validated_data["password2"]

        if password != password2:
            raise serializers.ValidationError({"error": "password do not match"})
        user.set_password(password)
        user.is_institutionStudent = True
        user.save()
        Student.objects.create(user=user)

        return user
