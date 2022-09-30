from django.urls import path
from .views import dashboard, create_shipment, receipt



urlpatterns = [
    path('create-shipment/', create_shipment, name="create-shipment" ),
    path('package/receipt/<int:id>', receipt, name="shipment-receipt" ),
    path('<str:username>/', dashboard, name="client-dashboard" ),
]