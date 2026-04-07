from rest_framework import generics
from .models import Transfer
from .serializers import TransferSerializer

from rest_framework import generics, permissions
from .models import Transfer
from .serializers import TransferSerializer


class TransferAPIView(generics.CreateAPIView):
    queryset = Transfer.objects.all()
    serializer_class = TransferSerializer
    permission_classes = [permissions.IsAuthenticated]