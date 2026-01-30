from django.urls import path
from todo_app import views

urlpatterns=[

    path('add/',views.addTask,name='addTask'),

    #mark_as_undone
    path('mark_as_done/<int:id>',views.mark_as_done,name='mark_as_done'),
    
    
    #mark_as_undone
    path('mark_as_undone/<int:id>',views.mark_as_undone,name='mark_as_undone'),



     #Edit feature
    path('edit_task/<int:id>',views.edit_task,name='edit_task'),


    path('delete_task/<int:id>',views.delete_task,name='delete_task'),


   

]