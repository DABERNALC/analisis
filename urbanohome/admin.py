from django.contrib import admin
from .models import Producto, Color, TipoIdentificacion, TipoProducto, Venta, Cliente
# Register your models here.
#DBCA was here!
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio_compra', 'precio_venta', 'stock', 'color')
    list_filter = ('nombre', 'precio_compra', 'precio_venta', 'stock')

class VentaAdmin(admin.ModelAdmin):
    list_display = ('id', 'clienteId', 'fecha', 'get_total')
    readonly_fields = ('id',)
    
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'celular', 'correo', 'identificacion')

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Color)
admin.site.register(TipoProducto)
admin.site.register(Venta, VentaAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(TipoIdentificacion)
