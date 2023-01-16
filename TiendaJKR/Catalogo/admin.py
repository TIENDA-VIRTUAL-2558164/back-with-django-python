from django.contrib import admin
from .models import producto_estado, marcas, tipos_producto, categorias, proveedores_estado, \
    proveedores, imagenes_estado, imagenes, comentarios, descuentos, descuentos_estado, productos

# Register your models here.
admin.site.register(producto_estado)
admin.site.register(marcas)
admin.site.register(tipos_producto)
admin.site.register(categorias)
admin.site.register(proveedores_estado)
admin.site.register(proveedores)
admin.site.register(imagenes_estado)
admin.site.register(imagenes)
admin.site.register(comentarios)
admin.site.register(descuentos)
admin.site.register(descuentos_estado)
admin.site.register(productos)
