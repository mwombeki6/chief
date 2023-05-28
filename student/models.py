from django.db import models
from django.utils.translation import gettext_lazy as _
from model.common_fields import BaseModel
from custom.models import User


class Student(BaseModel):
    """A Student model for storing Student information

    Args:
        BaseModel ([Student]): [Student information model]
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = _("Student")
