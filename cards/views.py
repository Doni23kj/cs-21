from rest_framework import generics, permissions
from .models import Card
from .serializers import CardSerializer


class CardAPIView(generics.CreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(client=self.request.user)