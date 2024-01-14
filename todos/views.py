from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Task

# Create your views here.
def addTask(request):
    task = request.POST['task']
    if task != '':
        Task.objects.create(task = task)
    
    return redirect('Home')

def mark_as_done(request, pk):
    task = get_object_or_404(Task,pk=pk)
    task.is_completed = True
    task.save()
    return redirect("Home") 

def mark_as_undone(request, pk):
    task = get_object_or_404(Task,pk=pk)
    task.is_completed = False
    task.save()
    return redirect("Home") 


def edit_task(request, pk):
    edited_task = request.POST['edited_task']
    task = get_object_or_404(Task, pk = pk)
    task.task = edited_task
    task.save()
    return redirect("Home")

def delete(request, pk):
    task = get_object_or_404(Task, pk = pk)
    task.delete()
    # task.save()
    return redirect("Home")
