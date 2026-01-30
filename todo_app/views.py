from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Task

# Create your views here.
def addTask(request):
   tasks= request.POST.get('task')
   Task.objects.create(task=tasks)
   return redirect('home')