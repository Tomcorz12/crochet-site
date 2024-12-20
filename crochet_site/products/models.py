from django.db import models

# Create your models here.
# Se crea modelo Producto
class Product(models.Model):
    name = models.TextField(max_length = 200, verbose_name = 'Nombre')
    description = models.TextField(max_length = 500, verbose_name = 'Descripción')
    price = models.DecimalField(max_digits = 10, decimal_places = 2, verbose_name = 'Precio') #Nos dejará agregar máximo dos decimales
    available = models.BooleanField(default = True, verbose_name = 'Disponible')
    photo = models.ImageField(upload_to = 'Logos', null = True, blank = True, verbose_name = 'Foto')
    
    def __str__(self):
        return self.name