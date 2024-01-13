from django.http import HttpResponse
from django.shortcuts import render 
from todos.models import Task

def Home(request):
    tasks = Task.objects.filter(is_completed = False).order_by('-created_at')
    context = {
        'tasks' : tasks,
    }
    return render(request, 'home.html', context) 