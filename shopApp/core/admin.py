from django.contrib import admin
from .models import Product,MainPhoto

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','category','created_at')
    list_filter = ('category', 'price')  
    search_fields = ('name', 'description')

@admin.register(MainPhoto)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('name','image')

