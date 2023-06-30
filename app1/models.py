from django.db import models

class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=8)

    class Meta:
        db_table = "tblUsuario"
