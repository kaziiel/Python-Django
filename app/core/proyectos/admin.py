from django.contrib import admin

#Importamos las clases desde los modelos
from .models import TipoDocu, CateProye, Proyectos, Documentos

# Register your models here.
# Registro del modelo de TipoDocu:
class TipoDocuModel(admin.ModelAdmin):
    list_display = ["NombTiDoc"]
    class Meta:
        model = TipoDocu

admin.site.register(TipoDocu)

# Registro del modelo de CateProye:
class CateProyeModel(admin.ModelAdmin):
    list_display = ["Lenguaje"]
    class Meta:
        model = CateProye

admin.site.register(CateProye)


# Registro del modelo de Proyectos:
class ProyectosModel(admin.ModelAdmin):
    list_display = ["NombProy"]
    class Meta:
        model = Proyectos

admin.site.register(Proyectos)


# Registro del modelo de Documentos:
class DocumentosModel(admin.ModelAdmin):
    list_display = ["NombDocu"]
    class Meta:
        model = Documentos

admin.site.register(Documentos)