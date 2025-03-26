from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Puesto(models.Model):
  name = models.CharField(max_length=100, verbose_name='Nombre')
  created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
  updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')

  class Meta:
    verbose_name: 'Puesto'
    verbose_name_plural: 'puestos'
    ordering = ['-created']

  def __str__(self):
    return self.name

class Area(models.Model):
  name = models.CharField(max_length=100, verbose_name='Nombre')
  created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
  updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')  

  class Meta:
    verbose_name: 'Area'
    verbose_name_plural: 'Areas'
    ordering = ['-created']
  
  def __str__(self):
    return self.name


class Worker(models.Model):
  name = models.CharField(max_length=100, verbose_name='Apellidos y Nombres')
  area = models.ManyToManyField(Area, verbose_name='Areas')
  puesto = models.ManyToManyField(Puesto, verbose_name='Puestos')
  active = models.CharField(max_length=20, verbose_name='Activo', default='SI')
  created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
  updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')

  class Meta:
    verbose_name = 'Trabajador'
    verbose_name_plural = 'Trabajadores'
    ordering = ['-created']

  def __str__(self):
    return self.name

class Marca(models.Model):
  name = models.CharField(max_length=100, verbose_name='Nombre')
  created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
  updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')  

  class Meta:
    verbose_name: 'Marca'
    verbose_name_plural = 'marcas'
    ordering = ['-created']
  
  def __str__(self):
    return self.name

class Category(models.Model):
  name = models.CharField(max_length=200, verbose_name='Título')
  created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
  updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')

  class Meta:
    verbose_name = 'categoría'
    verbose_name_plural = 'categorías'
    ordering = ['-created']

  def __str__(self):
    return self.name

class Processor(models.Model):
  name = models.CharField(max_length=200, verbose_name='Tipo')
  created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
  updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')

  class Meta:
    verbose_name = 'procesador'
    verbose_name_plural = 'procesadores'
    ordering = ['-created']

  def __str__(self):
    return self.name

class Ram(models.Model):
  name = models.CharField(max_length=200, verbose_name='Capacidad')
  created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
  updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')

  class Meta:
    verbose_name = 'ram'
    verbose_name_plural = 'rams'
    ordering = ['-created']

  def __str__(self):
    return self.name

class Disco(models.Model):
  name = models.CharField(max_length=200, verbose_name='Capacidad')
  created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
  updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')

  class Meta:
    verbose_name = 'disco'
    verbose_name_plural = 'discos'
    ordering = ['-created']

  def __str__(self):
    return self.name

class Warranty(models.Model):
  name = models.CharField(max_length=10, verbose_name='Garantía')
  created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
  updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')

  class Meta:
    verbose_name = 'garantia'
    verbose_name_plural = 'garantias'
    ordering = ['-created']

  def __str__(self):
    return self.name

class Mouse(models.Model):
  code = models.CharField(max_length=10, verbose_name='Código Mouse')
  name = models.CharField(max_length=100, verbose_name='Marca Mouse')
  created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
  updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')

  class Meta:
    verbose_name = 'mouse'
    verbose_name_plural = 'mouses'
    ordering = ['-created']

  def __str__(self):
    return self.code

class Keyboard(models.Model):
  code = models.CharField(max_length=10, verbose_name='Código Teclado')
  name = models.CharField(max_length=100, verbose_name='Marca Teclado')
  created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
  updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')

  class Meta:
    verbose_name = 'teclado'
    verbose_name_plural = 'teclados'
    ordering = ['-created']

  def __str__(self):
    return self.code

class Monitor(models.Model):
  code = models.CharField(max_length=10, verbose_name='Código Monitor')
  name = models.CharField(max_length=100, verbose_name='Marca Monitor')
  created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
  updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')

  class Meta:
    verbose_name = 'monitor'
    verbose_name_plural = 'monitores'
    ordering = ['-created']

  def __str__(self):
    return self.code

class Camera(models.Model):
  code = models.CharField(max_length=10, verbose_name='Código Cámara')
  name = models.CharField(max_length=100, verbose_name='Marca Cámara')
  created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
  updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')

  class Meta:
    verbose_name = 'camara'
    verbose_name_plural = 'camaras'
    ordering = ['-created']

  def __str__(self):
    return self.code

class Audifono(models.Model):
  code = models.CharField(max_length=10, verbose_name='Código Audífono')
  name = models.CharField(max_length=100, verbose_name='Marca Áudífono')
  created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
  updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')

  class Meta:
    verbose_name = 'audifono'
    verbose_name_plural = 'audifonos'
    ordering = ['-created']

  def __str__(self):
    return self.code

class Stabilizer(models.Model):
  code = models.CharField(max_length=10, verbose_name='Código Estabilizador')
  name = models.CharField(max_length=100, verbose_name='Marca Estabilizador')
  created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
  updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')

  class Meta:
    verbose_name = 'estabilizador'
    verbose_name_plural = 'estabilizadores'
    ordering = ['-created']

  def __str__(self):
    return self.code

class Supresor(models.Model):
  code = models.CharField(max_length=10, verbose_name='Código Supresor')
  name = models.CharField(max_length=100, verbose_name='Marca Supresor')
  created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
  updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')

  class Meta:
    verbose_name = 'supresor'
    verbose_name_plural = 'supresores'
    ordering = ['-created']

  def __str__(self):
    return self.code

class Cooler(models.Model):
  code = models.CharField(max_length=10, verbose_name='Código Cooler')
  name = models.CharField(max_length=100, verbose_name='Marca Cooler')
  created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
  updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')

  class Meta:
    verbose_name = 'cooler'
    verbose_name_plural = 'coolers'
    ordering = ['-created']

  def __str__(self):
    return self.code

class Device(models.Model):
  codigo = models.CharField(max_length=10, verbose_name='Código', null=False, blank=False)
  areas = models.ManyToManyField(Area, verbose_name='Areas')
  workers = models.ManyToManyField(Worker, verbose_name='Trabajadores')
  marcas = models.ManyToManyField(Marca, verbose_name='Marcas')
  categories = models.ManyToManyField(Category, verbose_name='Categorias')
  modelo = models.CharField(max_length=200, verbose_name='Modelo', null=True, blank=True)
  serie = models.CharField(max_length=200, verbose_name='Serie', null=True, blank=True, default='SOME STRING')
  processors = models.ManyToManyField(Processor, verbose_name='Procesador')
  rams = models.ManyToManyField(Ram, verbose_name='RAM')
  discos = models.ManyToManyField(Disco, verbose_name='Disco Duro')
  mouses = models.ManyToManyField(Mouse, verbose_name='Mouse', null=True, blank=True)
  teclados = models.ManyToManyField(Keyboard, verbose_name='Teclado')
  monitores = models.ManyToManyField(Monitor, verbose_name='Monitor')
  camaras = models.ManyToManyField(Camera, verbose_name='Camara')
  audifonos = models.ManyToManyField(Audifono, verbose_name='Audifono')
  estabilizadores = models.ManyToManyField(Stabilizer, verbose_name='Estabilizador')
  supresores = models.ManyToManyField(Supresor, verbose_name='Supresor de Pico')
  cooler = models.ManyToManyField(Cooler, verbose_name='Cooler')
  warrantys = models.ManyToManyField(Warranty, verbose_name='Grantía')
  tarjetaVideo = models.CharField(max_length=200, verbose_name='Tarjeta de Video', default='some string', null=True, blank=True)
  content = models.TextField(verbose_name='Observaciones', null=True, blank=True)
  image = models.ImageField(verbose_name='Imagen', upload_to='appInventario', null=True, blank=True)
  author = models.ForeignKey(User, verbose_name='Autor', on_delete=models.CASCADE)
  created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
  updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')

  class Meta:
    verbose_name='entrada'
    verbose_name_plural='entradas'
    ordering=['-created']
  
  def __str__(self):
    return self.codigo