from django.contrib import admin
from .models import Worker, Monitor

# Register your models here.
class WorkerAdmin(admin.ModelAdmin):
  readonly_fields = ('created', 'updated')

class MonitorAdmin(admin.ModelAdmin):
  readonly_fields = ('created', 'updated')
  list_display = ('codigo', 'monitor_workers', 'marca')
  ordering = ('codigo',)
  search_fields = ('codigo',)

  def monitor_workers(self,obj):
    return ', '.join([c.name for c in obj.workers.all().order_by('name')])
  monitor_workers.short_description = 'Usuario'

admin.site.register(Worker, WorkerAdmin)
admin.site.register(Monitor, MonitorAdmin)