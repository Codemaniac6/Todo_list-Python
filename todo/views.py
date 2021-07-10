from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
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


class TaskCreateView(CreateView):
    model = Task
    fields = '__all__'
    template_name = 'todo/task_create.html'
    success_url = reverse_lazy('task_list')


class TaskUpdateView(UpdateView):
    model = Task
    fields = '__all__'
    template_name = 'todo/task_create.html'
    success_url = reverse_lazy('task_list')


class TaskDeleteView(DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('task_list')
