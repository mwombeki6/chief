from django.db import models
from django.contrib.auth.models import AbstractUser

from .manager import UserManager


class User(AbstractUser):
    """Custom User  Model"""

    first_name = models.CharField(max_length=255, unique=True, null=True, blank=True)
    last_name = models.CharField(max_length=255, unique=True, null=True, blank=True)
    username = models.CharField(max_length=255, unique=True, null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)

    # Staff model fields
    employee_number = models.IntegerField(unique=True, null=True, blank=True)

    TITLE_SELECT = (
        ("Head Of Department", "Head Of Department"),
        ("Lecture", "Lecture"), 
    )
    title = models.CharField(max_length=100, choices=TITLE_SELECT, null=True, blank=True)

    education_background = models.TextField(max_length=255, null=True, blank=True)

    # Student model fields
    student_reg_no = models.IntegerField(unique=True, null=True, blank=True)
    CLASS_SELECT = (
        ("OD20-COE", "OD20-COE"),
        ("OD21-COE", "OD21-COE"),
        ("OD22-COE", "OD-22-COE"),
    )
    class_course = models.CharField(max_length=100, choices=CLASS_SELECT, null=True, blank=True)

    # Collective model fields
    DEPARTMENT_SELECT = (
        ("Computer Department", "Computer Department"),
        ("Mining Department", "Mining Department"),
        ("Mechanical Engineering Department", "Mechanical Engineering Department"),
        ("BioTech Department", "BioTech Department"),
    )
    department = models.CharField(max_length=100, choices=DEPARTMENT_SELECT, null=True, blank=True)

    is_active = models.BooleanField(default=True)

    GENDER_SELECT = (
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    )
    gender = models.CharField(max_length=100, choices=GENDER_SELECT, null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "first_name",
        "last_name",
        "username",
        #"employee_number",
        #"title",
        #"education_background",
        #"student_reg_no",
        #"class_course",
        #"department",
        #"gender",
    ]
    is_institutionStaff = models.BooleanField(default=False)
    is_institutionStudent = models.BooleanField(default=False)

    objects = UserManager()

    def __str__(self):
        return self.email
