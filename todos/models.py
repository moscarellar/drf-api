from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta

class Todo(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField(default="")
    deadline = models.DateTimeField(default=datetime.now() + timedelta(days=7))
    title = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)

    class Meta:
        ordering = ['deadline']
        app_label = 'todos'

    def __str__(self):
        return self.title