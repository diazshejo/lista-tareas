from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect  # Importa la función de redirección

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('lista_tareas'), name='root'),  # Redirige la raíz a lista de tareas
    path('tareas/', include('tareas.urls')),
]