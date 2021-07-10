from django.urls import path
from .views import TaskListView, TaskDetailView, TaskCreateView, TaskUpdateView, TaskDeleteView

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('task/<str:pk>', TaskDetailView.as_view(), name='task_detail'),
    path('task-create/', TaskCreateView.as_view(), name='task-create'),
    path('task-edit/<str:pk>', TaskUpdateView.as_view(), name='task-edit'),
    path('task-delete/<str:pk>', TaskDeleteView.as_view(), name='task-delete'),
]