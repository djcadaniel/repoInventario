from django.contrib import admin
from .models import Worker, CategoryComputer, Computer
from django.db.models.functions import Concat
from django.db.models import Value

# Register your models here.
class WorkerAdmin(admin.ModelAdmin):
  readonly_fields = ('created', 'updated')

class CategoryComputerAdmin(admin.ModelAdmin):
  readonly_fields = ('created', 'updated')

class ComputerAdmin(admin.ModelAdmin):
  readonly_fields = ('created', 'updated')
  list_display = ('codigo', 'computer_workers','computer_category', 'marca', 'modelo', 'serie', 'procesador', 'ram', 'discoduro', 'video', 'observaciones', 'garantia')
  ordering = ('codigo','marca')
  search_fields = ('codigo',)
  
  def computer_workers(self, obj):
    return ', '.join([c.name for c in obj.workers.all().order_by('name')])
  computer_workers.short_description = 'Usuario'

  def computer_category(self, obj):
    return ', '.join([c.name for c in obj.categoriesComputer.all().order_by('name')])
  computer_category.short_description = 'Tipo'

admin.site.register(Worker, WorkerAdmin)
admin.site.register(CategoryComputer, CategoryComputerAdmin)
admin.site.register(Computer, ComputerAdmin)