from django.urls import path
from todo_app import views

urlpatterns=[
    path('add/',views.addTask,name='addTask'),

]