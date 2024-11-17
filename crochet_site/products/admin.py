from django.contrib import admin
from .models import Product

# Register your models here.
# Agregamos una nueva clase que será para el producto
class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ['name', 'price']
    search_fields = ['name']

#Para terminar de registrarlo falta
#Nos permitirá hacer ediciones en el admin después de estarla utilizando
admin.site.register(Product, ProductAdmin)