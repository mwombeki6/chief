from django.db import models
from django.utils.translation import gettext_lazy as _
from model.common_fields import BaseModel
from custom.models import User


class Staff(BaseModel):
    """A Staff model for storing the institutionStaff information

    Args:
        BaseModel ([Staff]): [Staff information model]
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = _("Staff")
