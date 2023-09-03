from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.lista_tareas, name='lista_tareas'),
    path('crear/', views.crear_tarea, name='crear_tarea'),
    path('editar/<int:tarea_id>/', views.editar_tarea, name='editar_tarea'),
    path('eliminar/<int:tarea_id>/', views.eliminar_tarea, name='eliminar_tarea'),
]