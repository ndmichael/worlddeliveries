from django.contrib import admin
from .models import ItemSender, ItemDetail, ItemReciever, Status


class StatusInline(admin.TabularInline):
    model = Status


@admin.register(ItemDetail)
class ItemDetailAdmin(admin.ModelAdmin):
    model = ItemDetail
    list_display = ['item_name', 'quantity','description', 'weight',  'paid', 'item_code', 'date_sent', 'date_recieved']
    inlines = [StatusInline]
    prepopulated_fields = {"slug": ("item_name",)}


@admin.register(ItemSender)
class ItemSenderAdmin(admin.ModelAdmin):
    list_display = ['user', 'company', 'address','postal_code', 'country', 'city', 'date_sent']
    list_filter = ['user', 'country', 'date_sent']
    model = ItemDetail


@admin.register(ItemReciever)
class ItemRecieverAdmin(admin.ModelAdmin):
    list_display = ['sender', 'fullname', 'address','postal_code', 'country', 'city', 'date_created']
    list_filter = ['sender', 'date_created', 'country']
    list_editable = ['date_created', 'country']
