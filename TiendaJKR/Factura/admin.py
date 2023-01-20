from django.contrib import admin

from .models import factura_estado, detalle_factura, facturas

# Register your models here.

admin.site.register(factura_estado)
admin.site.register(detalle_factura)
admin.site.register(facturas)
