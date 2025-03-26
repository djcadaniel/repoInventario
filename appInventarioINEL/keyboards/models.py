from django.db import models

# Create your models here.
class Worker(models.Model):
  name = models.CharField(max_length=100)
  area = models.CharField(max_length=50, verbose_name='Área')
  cargo = models.CharField(max_length=50, verbose_name='Cargo')
  created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
  updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')

  class Meta:
    verbose_name = 'Trabajador'
    verbose_name_plural = 'Trabajadores'
    ordering = ['-created']

  def __str__(self):
    return self.name

class Keyboard(models.Model):
  codigo = models.CharField(max_length=7, verbose_name='Código')
  marca = models.CharField(max_length=100, verbose_name='Marca')
  workers = models.ManyToManyField(Worker, verbose_name='Trabajadores')
  created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
  updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')

  class Meta:
    verbose_name = 'Registro'
    verbose_name_plural = 'Registros'
    ordering = ['created']

  def __str__(self):
    return self.codigo