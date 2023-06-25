from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class TodoItem_model(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default = 1)
    task = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    deadline = models.DateTimeField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()  # Set the created_at field only when creating a new instance
        return super().save(*args, **kwargs)
