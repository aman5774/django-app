from django.db import models
from django.contrib.auth.models import User


class Priority(models.Model):
    """
    Model for Priority
    """
    label = models.CharField(max_length=10)

    def __str__(self):
        return self.label


class Task(models.Model):
    """
    Model for Task
    """
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    class Meta:
        ordering = ['timestamp', ]

    def __str__(self):
        return self.title
