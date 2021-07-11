from django.urls import path
from .views import *

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('task/<str:pk>', TaskDetailView.as_view(), name='task_detail'),
    path('task-create/', TaskCreateView.as_view(), name='task-create'),
    path('task-edit/<str:pk>', TaskUpdateView.as_view(), name='task-edit'),
    path('task-delete/<str:pk>', TaskDeleteView.as_view(), name='task-delete'),
    path('login/', TaskLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('signup/', RegistrationView.as_view(), name='signup'),
]