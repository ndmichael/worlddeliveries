from django.urls import path
from shipment.views import (
    index, track_item, editStatus,
    editSender, editClient, editItem,
)

# app_name = 'shop'

urlpatterns = [
    path('', index, name='shipment_index'),
    path('tracking/', track_item, name='shipment_track'),
    path('edit/sender/<str:slug>/<int:id>/', editSender, name='edit_sender'), 
    path('edit/client/<str:slug>/<int:id>/', editClient, name='edit_client'), 
    path('edit/item/<str:slug>/<int:id>/', editItem, name='edit_item'), 
    path('edit/status/<int:id>/', editStatus, name='edit_status'),  
]