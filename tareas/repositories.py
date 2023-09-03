from .models import Tarea

class TareaRepository:
    def listar_tareas(self):
        return Tarea.objects.all()

    def crear_tarea(self, descripcion, tipo_tarea, status, fecha):
        return Tarea.objects.create(descripcion=descripcion, tipo_tarea=tipo_tarea, status=status, fecha=fecha)

    def obtener_tarea(self, tarea_id):
        return Tarea.objects.get(pk=tarea_id)

    def actualizar_tarea(self, tarea_id, descripcion, tipo_tarea, status, fecha):
        tarea = Tarea.objects.get(pk=tarea_id)
        tarea.descripcion = descripcion
        tarea.tipo_tarea = tipo_tarea
        tarea.status = status
        tarea.fecha = fecha  # Agrega el valor de fecha
        tarea.save()

    def eliminar_tarea(self, tarea_id):
        tarea = Tarea.objects.get(pk=tarea_id)
        tarea.delete()

