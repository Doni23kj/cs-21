from django.db import models
from clients.models import Client


class Card(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="client_cards")
    number = models.CharField(max_length=16, unique=True, verbose_name="Номер карты")
    balance = models.IntegerField(default=0, verbose_name="Баланс")

    def __str__(self):
        return f"{self.client}"