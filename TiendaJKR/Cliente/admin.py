from django.contrib import admin

from .models import usuarios, usuario_estado, generos, tipo_documento, roles

# Register your models here.

admin.site.register(usuarios)
admin.site.register(usuario_estado)
admin.site.register(generos)
admin.site.register(tipo_documento)
admin.site.register(roles)
