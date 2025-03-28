from django.contrib import admin
from .models import Category, Device, Worker, Area, Marca, Processor, Ram, Disco, Warranty, Mouse, Keyboard, Monitor, Camera, Audifono, Stabilizer, Supresor, Cooler, Puesto


# Register your models here.
class PuestoAdmin(admin.ModelAdmin):
  readonly_fields = ('created', 'updated')

class AreaAdmin(admin.ModelAdmin):
  readonly_fields = ('created', 'updated')

class WorkerAdmin(admin.ModelAdmin):
  readonly_fields = ('created', 'updated')
  list_display = ('name','get_areas','get_puestos', 'updated')

  def get_puestos(self, obj):
    return ', '.join([c.name for c in obj.puesto.all().order_by('name')])
  get_puestos.short_description = 'Puesto'

  def get_areas(self, obj):
    return ', '.join([c.name for c in obj.area.all().order_by('name')])
  get_areas.short_description = 'Area'

class MarcaAdmin(admin.ModelAdmin):
  readonly_fields = ('created', 'updated')

class CategoryAdmin(admin.ModelAdmin):
  readonly_fields = ('created', 'updated')

class ProcessorAdmin(admin.ModelAdmin):
  readonly_fields = ('created', 'updated')

class RamAdmin(admin.ModelAdmin):
  readonly_fields = ('created', 'updated')

class DiscoAdmin(admin.ModelAdmin):
  readonly_fields = ('created', 'updated')
  list_display = ('name', 'created', 'updated')
  ordering = ('name', 'created', 'updated')
  search_fields = ('name',)
  date_hierarchy = 'created'
  list_filter = ('name',)

class WarrantyAdmin(admin.ModelAdmin):
  readonly_fields = ('created', 'updated')

class MouseAdmin(admin.ModelAdmin):
  readonly_fields = ('created', 'updated')
  list_display = ('code', 'name', 'created', 'updated')

class KeyboardAdmin(admin.ModelAdmin):
  readonly_fields = ('created', 'updated')
  list_display = ('code', 'name', 'created', 'updated')

class MonitorAdmin(admin.ModelAdmin):
  readonly_fields = ('created', 'updated')
  list_display = ('code', 'name', 'created', 'updated')

class CameraAdmin(admin.ModelAdmin):
  readonly_fields = ('created', 'updated')
  list_display = ('code', 'name', 'created', 'updated')

class AudifonoAdmin(admin.ModelAdmin):
  readonly_fields = ('created', 'updated')
  list_display = ('code', 'name', 'created', 'updated')

class StabilizerAdmin(admin.ModelAdmin):
  readonly_fields = ('created', 'updated')
  list_display = ('code', 'name', 'created', 'updated')

class SupresorAdmin(admin.ModelAdmin):
  readonly_fields = ('created', 'updated')
  list_display = ('code', 'name', 'created', 'updated')

class CoolerAdmin(admin.ModelAdmin):
  readonly_fields = ('created', 'updated')
  list_display = ('code', 'name', 'created', 'updated')

class DeviceAdmin(admin.ModelAdmin):
  readonly_fields = ('created', 'updated')
  list_display = ('codigo','device_categories','device_workers','device_areas', 'created', 'device_mouses','device_keyboards','device_camaras','device_audifonos','device_monitores','device_stabilizers','author')
  ordering = ('codigo',)
  search_fields = ('codigo',)


  def device_areas(self, obj):
    return ', '.join([c.name for c in obj.areas.all().order_by('name')])
  device_areas.short_description = 'Area'

  def device_workers(self, obj):
    return ', '.join([c.name for c in obj.workers.all().order_by('name')])
  device_workers.short_description = 'Usuario'

  def device_marcas(self, obj):
    return ', '.join([c.name for c in obj.workers.all().order_by('name')])
  device_areas.short_description = 'Marca'

  def device_categories(self, obj):
    return ', '.join([c.name for c in obj.categories.all().order_by('name')])
  device_categories.short_description = 'Categorías'

  def device_processors(self, obj):
    return ', '.join([c.name for c in obj.processors.all().order_by('name')])
  device_processors.short_description = 'Procesadores'

  def device_rams(self, obj):
    return ', '.join([c.name for c in obj.rams.all().order_by('name')])
  device_rams.short_description = 'RAMS'

  def device_discos(self, obj):
    return ', '.join([c.name for c in obj.discos.all().order_by('name')])
  device_discos.short_description = 'DISCO DUROS'

  def device_warrantys(self, obj):
    return ', '.join([c.name for c in obj.warrantys.all().order_by('name')])
  device_warrantys.short_description = 'Garantias'

  def device_mouses(self, obj):
    return ', '.join([c.code for c in obj.mouses.all().order_by('name')])
  device_mouses.short_description = 'Mouses'

  def device_keyboards(self, obj):
    return ', '.join([c.code for c in obj.teclados.all().order_by('name')])
  device_keyboards.short_description = 'Teclados'

  def device_monitores(self, obj):
    return ', '.join([c.code for c in obj.monitores.all().order_by('name')])
  device_monitores.short_description = 'Monitores'

  def device_camaras(self, obj):
    return ', '.join([c.code for c in obj.camaras.all().order_by('name')])
  device_camaras.short_description = 'Camaras'

  def device_audifonos(self, obj):
    return ', '.join([c.code for c in obj.audifonos.all().order_by('name')])
  device_audifonos.short_description = 'Audífonos'

  def device_stabilizers(self, obj):
    return ', '.join([c.code for c in obj.estabilizadores.all().order_by('name')])
  device_stabilizers.short_description = 'Estabilizadores'

  def device_supresores(self, obj):
    return ', '.join([c.code for c in obj.supresores.all().order_by('name')])
  device_supresores.short_description = 'Spresores'

  def device_coolers(self, obj):
    return ', '.join([c.code for c in obj.coolers.all().order_by('name')])
  device_coolers.short_description = 'Coolers'

admin.site.register(Puesto, PuestoAdmin)
admin.site.register(Area, AreaAdmin)
admin.site.register(Worker, WorkerAdmin)
admin.site.register(Marca, MarcaAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Processor, ProcessorAdmin)
admin.site.register(Ram, RamAdmin)
admin.site.register(Disco, DiscoAdmin)
admin.site.register(Warranty, WarrantyAdmin)
admin.site.register(Mouse, MouseAdmin)
admin.site.register(Keyboard, KeyboardAdmin)
admin.site.register(Monitor, MonitorAdmin)
admin.site.register(Camera, CameraAdmin)
admin.site.register(Audifono, AudifonoAdmin)
admin.site.register(Stabilizer, StabilizerAdmin)
admin.site.register(Supresor, SupresorAdmin)
admin.site.register(Cooler, CoolerAdmin)
admin.site.register(Device, DeviceAdmin)