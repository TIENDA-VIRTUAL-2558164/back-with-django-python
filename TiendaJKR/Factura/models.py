from django.db import models

# Create your models here.


class factura_estado(models.Model):
	nombre = models.CharField(max_length=45)
		

class detalle_factura (models.Model):
	cantidad = models.CharField(max_length=45)


class facturas(models.Model):
	fecha = models.DateTimeField()
	valor_compra = models.FloatField()
	# usuarios_id = models.ForeignKey('usuarios', on_delete=models.SET_NULL, null=True) campo por ajustar, se debe
	# averiguar como conectar con una tabla existente en otra app
	factura_estado_id = models.ForeignKey('factura_estado', on_delete=models.SET_NULL, null=True)
	# envios_id = models.ForeignKey('envios', on_delete=models.SET_NULL, null=True) campo por ajustar, se debe
	# averiguar como conectar con una tabla existente en otra app
