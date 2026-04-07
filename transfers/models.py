from django.db import models
from clients.models import Client


class Transfer(models.Model):
    sender = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="sender_transfers")
    receive = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="receive_transfers")
    amount = models.IntegerField(default=0, verbose_name="Сумма")

    def __str__(self):
        return f"{self.sender} -> {self.receive}"
