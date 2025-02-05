from django.shortcuts import render, reverse, redirect
from .models import Task
from .forms import TaskForm, TaskModelForm

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
        if 'saveTask' in request.POST:
            new_description = request.POST.get('task_description')
            new_done = request.POST.get('task_done')
            new_done = True if new_done == 'on' else False
            task.description = new_description
            task.done = new_done
            task.save()
            return redirect(reverse('home-view'))
        if 'deleteTask' in request.POST:
            task.delete()
            return redirect(reverse('home-view'))
    context = {
        'task': task
    }
    return render(request, 'tasks/detail_task.html', context)

def crate_form_task_view(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            description = form.cleaned_data['description'] 
            Task.objects.create(description=description)
            return redirect(reverse('home-view'))
    else:     
        form = TaskForm()    
    return render(request, 'tasks/crate_form_task.html', {'form': form})
