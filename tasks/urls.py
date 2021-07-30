from django.urls import path
from .views import (
    task_create,
    main,
    update_task,
    delete_task,
    search,
    complete_task,
    completed_list
)

urlpatterns = [
    path('completed/', completed_list, name='completed'),
    path('task/complete/<int:pk>', complete_task, name='complete_task'),
    path('search', search, name='search'),
    path('create-task/', task_create, name='task_create'),
    path('task/delete/<int:pk>', delete_task, name='task_delete'),
    path('task/<int:pk>', update_task, name='task_detail'),
    path('', main, name='main')
]
