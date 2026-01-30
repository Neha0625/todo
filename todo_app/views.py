from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Task

# Create your views here.
def addTask(request):
   tasks= request.POST.get('task')
   Task.objects.create(task=tasks)
   return redirect('home')

def mark_as_done(request,id):
   task= get_object_or_404(Task,id=id)
   task.is_completed=True
   task.save()
   return redirect('home')


def mark_as_undone(request,id):
   task=get_object_or_404(Task,id=id)
   task.is_completed=False
   task.save()
   return redirect('home')


def edit_task(request,id):
   get_task=get_object_or_404(Task,id=id)
   if request.method=='POST':
      new_task=request.POST['task']
      get_task.task=new_task
      get_task.save()
      return redirect('home')
   else:
      context={
         'get_task':get_task
         
      }
   return render(request,'edit_task.html',context)

def delete_task(request,id):
   task=get_object_or_404(Task,id=id)
   task.delete()
   return redirect('home')
   
   
   