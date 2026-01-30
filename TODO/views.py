from django.shortcuts import render
from todo_app.models import Task


def home(request):
    task=Task.objects.filter(is_completed=False).order_by('-task')
    completed_tasks=Task.objects.filter(is_completed=True)
    context={
        'task':task,
        'completed_tasks':completed_tasks
    }
    return render(request,'home.html',context)
 