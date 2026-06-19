from django.db import models
from django.contrib.auth.models import User, AbstractUser  

class User_Role(models.TextChoices):
    user = models.CharField(max_length=15, choices=[("user", "юзер")])
    moderator = models.CharField(max_length=15, choices=[("moderator", "модер")])
    admin = models.CharField(max_length=15, choices=[("admin", "адмін")])

class User(AbstractUser):
        
        role = models.ForeignKey(User_Role, on_delete=models.CASCADE)
        bio = models.TextField()

