from django.contrib.admin.sites import site
from django.db import models
from django.db.models.deletion import PROTECT
from django.db.models.fields import CharField
from django.core.validators import MinValueValidator

# Create your models here.
class TipoIdentificacion(models.Model):
    nombre = CharField(max_length=8)
    
    def __str__(self):
        return f'{self.nombre}'

class Cliente(models.Model):
    nombre = models.CharField(max_length=120)
    celular = models.CharField(max_length=14)
    correo = models.EmailField()
    identificacion = models.CharField(max_length=11, unique=True)
    
    def __str__(self):
        return f'{self.identificacion}'

class TipoProducto(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField()
    
    def __str__(self):
        return f'{self.nombre}'

class Color(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.nombre}'

class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    precio_compra = models.FloatField(max_length=12, validators=[MinValueValidator(0, "Ingrese un número positivo")])
    precio_venta = models.FloatField(max_length=12, validators=[MinValueValidator(0, "Ingrese un número positivo")])
    stock = models.IntegerField(validators=[MinValueValidator(0, "Ingrese un número positivo")])
    colorId = models.ForeignKey(Color, on_delete=models.PROTECT, verbose_name="Color")
    tipoProductoId = models.ForeignKey(TipoProducto, on_delete=PROTECT, verbose_name="Tipo")
    
    @property
    def color(self):
        return self.colorId
    
    def __str__(self):
        return f'{self.nombre}'
    
class Venta(models.Model):
    fecha = models.DateField()
    clienteId = models.ForeignKey(Cliente, on_delete=PROTECT)
    productoId = models.ManyToManyField(Producto, blank=True)
    
    @property
    def get_total(self):
        productos = self.productoId.all().values('precio_venta')
        total = 0
        for x in productos:
            total += x['precio_venta']
        return total
    
    def __str__(self):
        return f'{self.clienteId} - {self.fecha}'
    
    