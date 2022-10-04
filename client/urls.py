from django.urls import path
from .views import dashboard, create_shipment, receipt, del_package



urlpatterns = [
    path('create-shipment/', create_shipment, name="create-shipment" ),
    path('package/receipt/<int:id>', receipt, name="shipment-receipt" ),
    path('package/<int:id>/delete/', del_package, name="package-delete" ),
    path('<str:username>/', dashboard, name="client-dashboard" ),
]