from django.shortcuts import render
from todo_app.models import Task


def home(request):
    task=Task.objects.filter(is_completed=False).order_by('-task')
    context={
        'task':task
    }
    print(task)
    return render(request,'home.html',context)
 