from django.db import models

# Create your models here.
class Tarea(models.Model):
    ESTADO_CHOICES=[
        ('completado','Completado'),
        ('pendiente','Pendiente')
    ]
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=120)
    completado = models.CharField(max_length=100,choices=ESTADO_CHOICES)
