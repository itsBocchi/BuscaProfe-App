from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Agrega cualquier campo adicional que necesites para tu usuario

    def __str__(self):
        return self.user.username
