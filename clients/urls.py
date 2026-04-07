from django.urls import path
from .views import ClientListAPIView, ClientRetrieveAPIView, ClientRegisterAPIView

urlpatterns = [
    path('', ClientListAPIView.as_view(), name='client-list'),
    path('register/', ClientRegisterAPIView.as_view(), name='client-register'),
    path('<int:pk>/', ClientRetrieveAPIView.as_view(), name='client-detail'),
]