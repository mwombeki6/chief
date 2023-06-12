from django.db import models
from custom.models import User

class Notification(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    message = models.TextField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)
    is_viewed = models.BooleanField(default=False, db_index=True)

    def __str__(self) -> str:
        return f"{self.user}: {self.title}"