from rest_framework import serializers
from django.db import transaction
from .models import Transfer


class TransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transfer
        fields = ("id", "receive", "amount")

    def validate(self, attrs):
        request = self.context.get("request")
        sender = request.user
        receive = attrs.get("receive")
        amount = attrs.get("amount")

        if sender == receive:
            raise serializers.ValidationError("Өзүңө өзүң акча которо албайсың.")

        if amount <= 0:
            raise serializers.ValidationError("Сумма 0 ден чоң болушу керек.")

        if sender.balance < amount:
            raise serializers.ValidationError("Баланста акча жетишсиз.")

        return attrs

    @transaction.atomic
    def create(self, validated_data):
        request = self.context.get("request")
        sender = request.user
        receive = validated_data["receive"]
        amount = validated_data["amount"]

        sender.balance -= amount
        receive.balance += amount

        sender.save()
        receive.save()

        transfer = Transfer.objects.create(
            sender=sender,
            receive=receive,
            amount=amount
        )
        return transfer