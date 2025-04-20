from django.contrib import admin
from .models import Product

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','category','created_at')
    list_filter = ('category', 'price')  # Теперь можно фильтровать по категориям
    search_fields = ('name', 'description')
