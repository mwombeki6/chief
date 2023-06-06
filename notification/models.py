from django.db import models
from custom.models import User

class Notification(models.Model):
    recipient = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)
    is_viewed = models.BooleanField(default=False, db_index=True)

    def __str__(self) -> str:
        return f"{self.recipient}: {self.title}"