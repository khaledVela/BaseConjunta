from django.db import models


# Create your models here.
class Users_rol(models.Model):
    user_id = models.IntegerField()
    rol_id = models.IntegerField()
    usuario = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

class Recidencia(models.Model):
    recidencia_id = models.IntegerField()
    condominio_id = models.IntegerField()


class AreaComun(models.Model):
    AreaComun_id = models.IntegerField()
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    capacidad = models.IntegerField()
    turno = models.CharField(max_length=50)
    estado = models.IntegerField()
    user_id = models.IntegerField()
