from django.db import models
from django.contrib.auth.models import User, AbstractUser  

class User_Role(models.TextChoices):
    USER = "user", "юзер"
    MODERATOR = "moderator", "модер"
    ADMIN = "admin", "адмін"\

class User(AbstractUser):
        
        role = models.ForeignKey(User_Role, on_delete=models.CASCADE)
        bio = models.TextField()
