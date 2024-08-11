from django.db import models

# Create your models here.

# myapp/models.py
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    qualification = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.user.username}: {self.qualification}'
