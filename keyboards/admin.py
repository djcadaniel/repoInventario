from django.contrib import admin
from .models import Worker, Keyboard

# Register your models here.
class WorkerAdmin(admin.ModelAdmin):
  readonly_fields = ('created', 'updated')

class KeyboardAdmin(admin.ModelAdmin):
  readonly_fields = ('created', 'updated')
  list_display = ('codigo', 'keyboard_workers', 'marca')
  ordering = ('codigo',)
  search_fields = ('codigo',)

  def keyboard_workers(self,obj):
    return ', '.join([c.name for c in obj.workers.all().order_by('name')])
  keyboard_workers.short_description = 'Usuario'

admin.site.register(Worker, WorkerAdmin)
admin.site.register(Keyboard, KeyboardAdmin)