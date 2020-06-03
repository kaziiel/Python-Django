from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
#Se importa el modelo de la otra app
from userdata.models import DatosUser
# Create your models here.

class TipoDocu(models.Model):
    NombTiDoc = models.CharField(max_length = 45, verbose_name = "Nombre tipo documento")

    class Meta:
        verbose_name = "Tipo documento"
        verbose_name_plural = "Tipos de documentos"
    
    #Funcion para llamar atributos:
    def __str__(self):
        return self.NombTiDoc

class CateProye(models.Model):
    Lenguaje = models.CharField(max_length = 45, verbose_name= "Lenguaje de programacion")
    MotorDB = models.CharField(max_length= 155,verbose_name= "Motor de base de datos" )
    Arquitectura = models.CharField(max_length= 255, verbose_name="Aquitectura de software")

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
    
    #Funcion para llamar atributos:
    def __str__(self):
        return self.Lenguaje

class Proyectos(models.Model):
    idCategProye = models.ForeignKey(CateProye, on_delete = models.CASCADE, verbose_name = "Identificador de categoria de proyectos")
    NombProy = models.CharField(max_length=255, verbose_name="Nombre del proyecto")
    DescProy = models.TextField(max_length= 2000, verbose_name="Descripcion del proyecto")
    ImgPorye = models.ImageField(default = 'proy.png' , verbose_name = "Foto del proyecto", upload_to = "proyectoImg")
    FechaIni = models.DateField(auto_now_add = True, null = True, verbose_name= "Iniciado el")
    FechaFin = models.DateField(auto_now = True, null = True, verbose_name= "Terminado el")
    UrlRepo = models.TextField(max_length=2000, verbose_name="Link del repositorio")
    EstaProy = models.CharField(max_length=45, verbose_name="Estado del proyecto")

    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"
    
    #Funcion para llamar atributos:
    def __str__(self):
        return self.NombProy


class Documentos(models.Model):
    idTipoDocu = models.ForeignKey(TipoDocu, on_delete = models.CASCADE, verbose_name = "Identificador del tipo de documento")
    idProyectos = models.ForeignKey(Proyectos, on_delete = models.CASCADE, verbose_name = "Identificador de proyecto")
    idUsuarios = models.ForeignKey(DatosUser, on_delete = models.CASCADE, verbose_name = "Identificador de usuario")
    NombDocu = models.CharField(max_length=255, verbose_name="Nombre del documento")
    PathDocu = models.FileField(max_length=45, upload_to= None,verbose_name= "Ruta del documento")

    class Meta:
        verbose_name = "Documento"
        verbose_name_plural = "Documentos"
    
    #Funcion para llamar atributos:
    def __str__(self):
        return self.NombDocu

    
    

