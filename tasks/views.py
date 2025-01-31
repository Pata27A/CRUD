from django.shortcuts import render, reverse, redirect
from .models import Task

def home_view(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, 'tasks/home.html', context)

def create_task_view(request):
    if request.method == "POST":  # Usar request.method para evitar posibles errores
        new_task = request.POST.get('task')  # Corregir el nombre de la variable
        if new_task:  # Asegurarse de que no sea vacío
            Task.objects.create(description=new_task)  # Corregir el nombre del campo
        return redirect(reverse('home-view'))
    
    return render(request, 'tasks/create_task.html')

def detail_task_view(request, pk):
    task = Task.objects.get(id=pk)

    if request.POST:
        new_description = request.POST.get('task_description')
        new_done = request.POST.get('task_done')
        if new_done == 'on':
            new_done = True
        else:
            new_done = False
        task.description = new_description
        task.done = new_done
        task.save()
        return redirect(reverse('home-view'))

    context = {
        'task': task
    }
    return render(request, 'tasks/detail_task.html', context)
