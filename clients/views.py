from rest_framework import generics, permissions
from .models import Client
from .serializers import ClientSerializer, ClientRegisterSerializer


class ClientListAPIView(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated]


class ClientRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated]


class ClientRegisterAPIView(generics.CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientRegisterSerializer
    permission_classes = [permissions.AllowAny]