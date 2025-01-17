from django.shortcuts import render,get_object_or_404, redirect

from django.http import HttpResponse
from .models import Task
from .forms import TaskForm

# Create your views here.

def hellowold(request):
    return HttpResponse('HelloWord')

def taskList(request):
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'tasks/list.html',{'tasks' : tasks } )

def yourName(request , name):
    return render(request , 'tasks/yourname.html',{'name':name})

def showTask(request, id):
    task = get_object_or_404(Task , pk=id)
    return render(request , 'tasks/showtask.html',{'task':task})

def newTask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.done = 'doing'
            task.save()
            return redirect('/')
    else:
        form = TaskForm()
        return render(request , 'tasks/addTask.html',{'form':form})

def deleteTask(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()
    return redirect('/')

def editTask(request, id):
    task = get_object_or_404(Task, pk=id)
    form = TaskForm(instance=task)
    #se for post entao estah a fazer o update
    if(request.method == 'POST'):
        form = TaskForm(request.POST , instance=task)
        if(form.is_valid()):
            task.save()
            return redirect('/')
        else:
            return render(request , 'tasks/editTask.html', {'form':form, 'task':task})    
    
    #senao, ainda estamos no edit
    else:
        return render(request , 'tasks/editTask.html', {'form':form, 'task':task})

