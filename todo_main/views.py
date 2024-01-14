from django.http import HttpResponse
from django.shortcuts import render 
from todos.models import Task

def Home(request):
    tasks = Task.objects.filter(is_completed = False).order_by('-created_at')
    is_completed = Task.objects.filter(is_completed = True)
    context = {
        'tasks' : tasks,
        'completed_tasks' : is_completed,
    }
    print(is_completed)
    return render(request, 'home.html', context) 