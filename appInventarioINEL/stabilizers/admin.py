from django.contrib import admin
from .models import Worker, Stabilizer

# Register your models here.
class WorkerAdmin(admin.ModelAdmin):
  readonly_fields = ('created', 'updated')

class StabilizerAdmin(admin.ModelAdmin):
  readonly_fields = ('created', 'updated')
  list_display = ('codigo', 'stabilizers_workers', 'marca')
  ordering = ('codigo',)
  search_fields = ('codigo',)

  def stabilizers_workers(self,obj):
    return ', '.join([c.name for c in obj.workers.all().order_by('name')])
  stabilizers_workers.short_description = 'Usuario'

admin.site.register(Worker, WorkerAdmin)
admin.site.register(Stabilizer, StabilizerAdmin)