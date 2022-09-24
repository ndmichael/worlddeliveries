from django.urls import path
from .views import dashboard, create_shipment



urlpatterns = [
    path('create-shipment/', create_shipment, name="create-shipment" ),
    path('<str:username>/', dashboard, name="client-dashboard" ),
]