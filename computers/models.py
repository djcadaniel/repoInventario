from django.db import models

# Create your models here.
class Worker(models.Model):
  name = models.CharField(max_length=100, verbose_name='Nombre')
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

class CategoryComputer(models.Model):
  name = models.CharField(max_length=100, verbose_name='Nombre')
  created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
  updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')

  class Meta:
    verbose_name = 'Categoria'
    verbose_name_plural = 'Categorias'
    ordering = ['-created']

  def __str__(self):
    return self.name

class Computer(models.Model):
  codigo = models.CharField(max_length=7, verbose_name='Codigo')
  marca = models.CharField(max_length=100, verbose_name='Marca')
  modelo = models.CharField(max_length=200, verbose_name='Modelo')
  serie = models.CharField(max_length=200, verbose_name='Serie')
  procesador = models.CharField(max_length=200, verbose_name='Procesador')
  ram = models.CharField(max_length=200, verbose_name='RAM')
  discoduro = models.CharField(max_length=200, verbose_name='Disco Duro')
  video = models.CharField(max_length=200, verbose_name='Tarjeta de Video')
  observaciones = models.CharField(max_length=1000, verbose_name='Observaciones')
  garantia = models.CharField(max_length=1000, verbose_name='Garantía')
  workers = models.ManyToManyField(Worker, verbose_name='Trabajadores')
  categoriesComputer = models.ManyToManyField(CategoryComputer, verbose_name='Categorías')
  created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
  updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')

  class Meta:
    verbose_name = 'Registro'
    verbose_name_plural = 'Registros'
    ordering= ['-created']
  
  def __str__(self):
    return self.codigo