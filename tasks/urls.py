from django.urls import path
from tasks.views import*
from . import views

urlpatterns = [
    path('', views.task_list, name='task-list'),
    path('create/', views.task_create, name='task-create'),
    path('signup/', views.signup, name='signup'),
]
