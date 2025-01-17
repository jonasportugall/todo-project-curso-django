from django.urls import path

from . import views

urlpatterns = [
    path('hellowold/', views.hellowold),
    path('',views.taskList, name='task-list'),
    path('task/<int:id>', views.showTask, name="show-task"),
    path('yourname/<str:name>',views.yourName, name='your-name'),
    path('newTask/',views.newTask, name="new-task"),
    path('edit/<int:id>',views.editTask, name="edit-task"),
    path('delete/<int:int>',views.deleteTask,name="delete-task")
]

