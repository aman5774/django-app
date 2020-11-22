from django.urls import path
from .views import task_create, task_list

# app name to be used for url templating
app_name = 'tasks'

urlpatterns = [
    path('', task_list, name="list"),
    path('create', task_create, name="create"),
]
