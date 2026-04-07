from rest_framework import serializers
from .models import Client
from cards.serializers import CardSerializer


class ClientSerializer(serializers.ModelSerializer):
    client_cards = CardSerializer(many=True, read_only=True)

    class Meta:
        model = Client
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "age",
            "email",
            "phone",
            "balance",
            "avatar",
            "address",
            "client_cards",
        )


class ClientRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Client
        fields = (
            "id",
            "username",
            "password",
            "first_name",
            "last_name",
            "age",
            "email",
            "phone",
            "balance",
            "avatar",
            "address",
        )

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = Client(**validated_data)
        user.set_password(password)
        user.save()
        return user