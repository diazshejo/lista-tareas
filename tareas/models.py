from django.db import models
from django.utils import timezone

class Tarea(models.Model):
    descripcion = models.CharField(max_length=256)
    tipo_tarea = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    fecha = models.DateTimeField()

    def __str__(self):
        return self.descripcion