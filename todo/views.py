from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, DetailView
from .models import Task


def home(request):
    return HttpResponse('To-do List')


class TaskListView(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'todo/task_list.html'


class TaskDetailView(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'todo/task_detail.html'
