from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    username = models.CharField(max_length=50, unique=True, verbose_name="логин")
    email = models.EmailField(unique=True, verbose_name="почта")
    phone = models.CharField(
        max_length=35, blank=True, null=True, verbose_name="телефон"
    )
    birth_date = models.DateField(verbose_name="дата рождения", blank=True, null=True)
    creation_date = models.DateField(
        verbose_name="дата создания", blank=True, null=True
    )
    modif_date = models.DateField(
        verbose_name="дата редактирования", blank=True, null=True
    )

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    class Mera:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"
