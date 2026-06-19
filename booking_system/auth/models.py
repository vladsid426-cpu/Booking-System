from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserRole(models.TextChoices):
    USER = "user", _("юзер")
    MODERATOR = "moderator", _("модер")
    ADMIN = "admin", _("адмін")


class User(AbstractUser):
    role = models.CharField(
        max_length=15,
        choices=UserRole.choices,
        default=UserRole.USER.value,
        verbose_name=_("Роль"),
    )
    bio = models.TextField(blank=True, verbose_name=_("Біографія"))

    class Meta:
        verbose_name = _("Користувач")
        verbose_name_plural = _("Користувачі")

    def __str__(self):
        return self.username