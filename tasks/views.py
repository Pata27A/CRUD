from django.shortcuts import render, reverse, redirect
from .models import Task

def home_view(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
   }
    return render(request, 'tasks/home.html', context)

def create_task_view(request):
    if request.POST:
        new_tasK = request.POST.get('task')
        Task.objects.create(desciption=new_tasK)
        return redirect(reverse('home-view'))
    return render(request, 'tasks/create_task.html')