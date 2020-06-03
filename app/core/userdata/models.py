from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
from .genero import Generos

# Create your models here.
# Crear la estructura de la aplicacion en el modelo de datos 

class Roles(models.Model):
    RoleName = models.CharField(max_length = 50)

    class Meta:
        verbose_name = "Perfil de Usuario"
        verbose_name_plural = "Perfiles"


    # Se crea la funcón para llamar atributos:
    def __str__(self):
        return self.RoleName

# Modelo de la tabla datos de usuario
class DatosUser(models.Model):
    UserDNI = models.CharField(max_length = 20, verbose_name= "Identificación") 
    nombUser = models.CharField(max_length= 256,null = True, verbose_name= "Nombres")
    apelUser = models.CharField(max_length=256,null = True, verbose_name= "Apellidos")
    profeUser = models.CharField(max_length= 100, null = True, verbose_name= "Profesión")
    FotoUser = models.ImageField(default='user.png', verbose_name = "Foto de perfil", upload_to="perfil")
    TeleUser = models.CharField(max_length = 20, verbose_name= "Número de Teléfono")
    geneUser = models.CharField(max_length = 20, choices= Generos, default = "Otro", verbose_name="Género")
    addData = models.DateTimeField(auto_now_add = True, null = True, verbose_name= "Creado el")
    modifiat = models.DateTimeField(auto_now = True, null = True, verbose_name= "Modificado el")

    class Meta:
        verbose_name = "Datos de Usuario"
        verbose_name_plural = "Información"

    #función
    def __str__(self):
        return self.nombUser
# Modelo de la tabla habilidades
class HabilUser(models.Model):
    NombHabil = models.CharField(max_length = 100, verbose_name= "Competencia")
    Prof = models.CharField(max_length= 100, null = True, verbose_name= "Profesión")
    DescHabil = models.TextField(max_length= 2000, verbose_name= "Descripción de la habilidad")

    class Meta:
        verbose_name = "Habilidades del Usuario"
        verbose_name_plural = "Competencias"

    #función
    def __str__(self):
        return self.NombHabil
# Modelo de detalle de roles
class DetaRoles(models.Model):
    idRole = models.ForeignKey(Roles, on_delete = models.CASCADE, verbose_name = "Identificador de Rol")
    idUser = models.ForeignKey(DatosUser, on_delete = models.CASCADE, verbose_name = "Identificador de Usuario")
    addUser = models.DateTimeField(auto_now_add = True, null = True, verbose_name = "Creado el")
    udtUser = models.DateTimeField(auto_now= True,null = True, verbose_name = "Modificador el")
    estaRol = models.CharField(max_length= 10, verbose_name = "Estado")

    class Meta: 
        verbose_name = "Roles de Usuario"
        verbose_name_plural = "Roles"
    
    #funcion
    def __str__(self):
        return self.idUser

# Modelo de calificaciones
class Rates(models.Model):
    idHabil = models.ForeignKey(HabilUser, on_delete = models.CASCADE, verbose_name = "Identificador de Habilidad")
    idUser = models.ForeignKey(DatosUser, on_delete= models.CASCADE, verbose_name = "Identificador de Usuario")
    pcrHabil = models.DecimalField(max_digits = 2, decimal_places = 1, verbose_name = "Porcentaje") #99,9
    udtHabil = models.DateTimeField(auto_now = True,null = True, verbose_name = "")

    class Meta:
        verbose_name = "Porcentaje de nivel de Habilidad"
        verbose_name_plural = "Niveles de Usuario"

    #funcion
    def __str__(self):
        return self.idUser 