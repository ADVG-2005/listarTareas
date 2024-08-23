from django.shortcuts import render, redirect
from .form import TareaForm
from .models import Tarea
# Create your views here.

def crearTarea(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar')
    form = TareaForm()
    return render(request, 'crearTarea.html',{'form': form})
def listarTarea(request):
    tareas = Tarea.objects.all()
    return render(request,'listarTarea.html',{'tareas': tareas})

