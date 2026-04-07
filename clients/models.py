from django.db import models
from django.contrib.auth.models import AbstractUser


class Client(AbstractUser):
    age = models.IntegerField(default=0, verbose_name="Возраст")
    phone = models.CharField(max_length=255, blank=True, verbose_name="Номер телефона")
    balance = models.IntegerField(default=0, verbose_name="Баланс")
    avatar = models.FileField(upload_to="avatar", blank=True, verbose_name="Аватар")
    address = models.CharField(max_length=255, blank=True, verbose_name="Адрес")

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.first_name} - {self.last_name}"

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Client"

