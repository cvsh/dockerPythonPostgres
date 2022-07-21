from django.contrib import admin

# Register your models here.
from .models import Orders

class orderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'date', 'price_usd', 'price_rub',)

admin.site.register(Orders, orderAdmin)