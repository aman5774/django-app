from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import forms
from .models import Task


@login_required(login_url="accounts/login")
def task_list(request):
    """
    List all the tasks created by user.
    :param request: request object
    :return: template with rendered list of all the tasks
    """
    try:
        # fetch all the tasks
        tasks = Task.objects.all()
        return render(request, 'tasks/list_tasks.html', {'tasks': tasks})
    except Exception as e:
        # Todo: change this to redirect at error page
        return redirect('accounts:login')


@login_required(login_url="accounts/login")
def task_create(request):
    """
    Create the task for the user.
    :param request: request object
    :return:
    GET: template to render create task form
    POST: Save the user task and redirect to tasks page
    """
    try:
        if request.method == "POST":
            form = forms.CreateTask(data=request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                # adding author to the task
                instance.author = request.user
                form.save()
                return redirect('tasks:list')
        else:
            # create task form
            task_form = forms.CreateTask()
            return render(request, 'tasks/create_task.html', {'form': task_form})
    except Exception as e:
        # Todo: change this to redirect at error page
        return redirect('accounts:login')
