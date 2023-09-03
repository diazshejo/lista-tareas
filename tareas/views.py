from django.shortcuts import render, redirect
from .repositories import TareaRepository

def lista_tareas(request):
    tarea_repo = TareaRepository()
    tareas = tarea_repo.listar_tareas()
    return render(request, 'tareas/lista_tareas.html', {'tareas': tareas})

def crear_tarea(request):
    if request.method == 'POST':
        descripcion = request.POST.get('descripcion')
        tipo_tarea = request.POST.get('tipo_tarea')
        status = request.POST.get('status')
        fecha = request.POST.get('fecha')  # Agrega esta línea

        tarea_repo = TareaRepository()
        tarea_repo.crear_tarea(descripcion, tipo_tarea, status, fecha)  # Pasa la fecha

        return redirect('lista_tareas')

    return render(request, 'tareas/crear_tarea.html')

def editar_tarea(request, tarea_id):
    tarea_repo = TareaRepository()
    tarea = tarea_repo.obtener_tarea(tarea_id)

    if request.method == 'POST':
        descripcion = request.POST.get('descripcion')
        tipo_tarea = request.POST.get('tipo_tarea')
        status = request.POST.get('status')
        fecha = request.POST.get('fecha')  # Agrega esta línea

        tarea_repo.actualizar_tarea(tarea_id, descripcion, tipo_tarea, status, fecha)  # Pasa la fecha

        return redirect('lista_tareas')

    return render(request, 'tareas/editar_tarea.html', {'tarea': tarea})

def eliminar_tarea(request, tarea_id):
    tarea_repo = TareaRepository()
    tarea_repo.eliminar_tarea(tarea_id)
    return redirect('lista_tareas')
