from django.db.models.signals import pre_delete
from django.dispatch import receiver
from .models import Tarea, Usuario
#Aprender bien
@receiver(pre_delete, sender=Usuario)
def borrar_tareas(sender, instance, **kwargs):
    tarea = Tarea.objects.filter(
        id__in = instance.tiene.values_list('tarea_id', flat=True)
    )
    tarea.delete