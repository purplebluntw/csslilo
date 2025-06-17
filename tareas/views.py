from django.shortcuts import render
from django.shortcuts import redirect
import uuid
from datetime import date

# tareas/views.py
from django.http import HttpResponse
from django.http import Http404
from .models import Tarea
from django.template import loader

def login(request):
    return render(request, "tareas/trueIndex.html")

def index(request):
    tareas = Tarea.objects.order_by("-id")
    template = loader.get_template("tareas/index.html")
    context = {"tareas": tareas}
    return HttpResponse(template.render(context, request))

    #return HttpResponse(", ".join([f"{tarea.id} - {tarea.titulo} - Completado: {tarea.completado}" for tarea in Tarea.objects.all()]))
def editar(request, id):
    try:
        tarea = Tarea.objects.get(pk=id)
        if request.method == 'POST':
            tarea.titulo = request.POST.get('titulo')
            tarea.completado = 'completado' in request.POST
            tarea.save()
            return redirect('index')
        return render(request, "tareas/editar.html", {"tarea": tarea})
    except Tarea.DoesNotExist:
        raise Http404("Tarea no encontrada")
    
def crear(request):
    if request.method == 'POST':
        tarea = Tarea(
            titulo = request.POST.get('titulo'),
            completado = 'completado' in request.POST,
            uuid = str(uuid.uuid4()),
            important = 'importante' in request.POST,
            fecha=date.today()
        )
        tarea.save()
        return redirect('index')
    return render(request, "tareas/crear.html")

def borrar(request, id):
    tarea = Tarea.objects.get(pk=id)
    if request.method == 'POST':
        tarea.delete()
        return redirect('index')
    return redirect('index')