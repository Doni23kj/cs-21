from django.urls import path
from .views import TransferAPIView

urlpatterns = [
    path('create/', TransferAPIView.as_view(), name='create'),
]