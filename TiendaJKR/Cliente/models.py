from django.db import models


# Create your models here.
class usuario_estado(models.Model):
	estatus = models.CharField(max_length=45)
	
	def __str__(self):
		return self.estatus


class generos(models.Model):
	genero = models.CharField(max_length=15)
	
	def __str__(self):
		return self.genero


class tipo_documento(models.Model):
	tipo_doc = models.CharField(max_length=45)
	
	def __str__(self):
		return self.tipo_doc


class roles(models.Model):
	rol = models.CharField(max_length=20)
	
	def __str__(self):
		return self.rol


class usuarios(models.Model):
	nombres = models.CharField(max_length=45)
	apellidos = models.CharField(max_length=45)
	num_documento = models.IntegerField()
	correo = models.CharField(max_length=125)
	contrasena = models.CharField(max_length=16)
	num_contacto = models.IntegerField()
	edad = models.DateField()
	direccion = models.CharField(max_length=45)
	usuario_estado_id = models.ForeignKey('usuario_estado', on_delete=models.SET_NULL, null=True)
	genero_id = models.ForeignKey('generos', on_delete=models.SET_NULL, null=True)
	tipo_documento_id = models.ForeignKey('tipo_documento', on_delete=models.SET_NULL, null=True)
	rol_id = models.ForeignKey('roles', on_delete=models.SET_NULL, null=True)
	
