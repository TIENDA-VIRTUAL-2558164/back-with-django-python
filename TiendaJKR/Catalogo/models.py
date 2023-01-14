from django.db import models

# Create your models here.


class producto_estado(models.Model):
    nombre = models.CharField(max_length=45)


class marcas(models.Model):
    marca = models.CharField(max_length=45)


class tipos_producto(models.Model):
    tipo = models.CharField(max_length=45)


class categorias(models.Model):
    categoria = models.CharField(max_length=45)


class proveedores_estado(models.Model):
    prov_estado = models.CharField(max_length=45)


class proveedores(models.Model):
    proveedor = models.CharField(max_length=45)
    proveedor_estado_id = models.ForeignKey('proveedores_estado', on_delete=models.SET_NULL, null=True)


class imagenes_estado(models.Model):
    img_estado = models.CharField(max_length=45)


class imagenes(models.Model):
    imagen = models.TextField()
    imagen_estado = models.ForeignKey('imagenes_estado', on_delete=models.SET_NULL, null=True)


class comentarios(models.Model):
    comentario = models.TextField()
    comentario_id = models.IntegerField(max_length=45)
    usuarios_id = models.IntegerField()


class descuentos(models.Model):
    descuento = models.CharField(45)
    fecha_inicio = models.DateField() ##pendiente definir el formato de fecha
    fecha_final = models.DateField() #pendiente definir el formato de fecha
    porcentaje = models.CharField(max_length=45)
    descuento_estado_id = models.ForeignKey('descuentos_estado', on_delete=models.SET_NULL, null=True)


class descuentos_estado(models.Model):
    dto_estado = models.CharField(max_length=45)
