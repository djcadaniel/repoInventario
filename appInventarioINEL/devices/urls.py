from django.urls import path
from . import views

urlpatterns = [
  path('', views.usuario, name='usuario'),
  path('computadora', views.computadora, name='computadora'),
  path('mouse', views.mouse, name='mouse'),
  path('teclado', views.teclado, name='teclado'),
  path('monitor', views.monitor, name='monitor'),
  path('camara', views.camara, name='camara'),
  path('audifono', views.audifono, name='audifono'),
  path('estabilizador', views.estabilizador, name='estabilizador'),
  path('cooler', views.cooler, name='cooler'),
  path('supresor', views.supresor, name='supresor'),

  path('export-to-excel/', views.export_excel_workers, name='export_to_excel'),
]