from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


class CustomUser(AbstractUser):
    """Модель пользователей."""

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    mail = models.EmailField(
        max_length=254,
        unique=True,
        blank=False,
    )
    first_name = models.CharField(
        max_length=150,
        unique=True,
        blank=False,
    )
    last_name = models.CharField(
        max_length=150,
        unique=True,
        blank=False,
    )
    password = models.CharField(
        max_length=150,
        blank=False,
        validators=[
            RegexValidator(r'^[\w.@+-]+\Z'),
        ],
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('username',)

    def __str__(self) -> str:
        return self.username
