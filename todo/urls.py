from django.urls import path
from .views import TaskListView, TaskDetailView

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('task/<str:pk>', TaskDetailView.as_view(), name='task_detail')
]