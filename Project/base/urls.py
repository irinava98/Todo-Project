from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, CustomLoginView, RegisterPage, \
    add_default_categories_tags, TaskReorder
from django.contrib.auth import logout


# Custom logout view
def custom_logout_view(request):
    logout(request)
    return redirect('login')


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', custom_logout_view, name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),

    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name='task-delete'),
    path('task-reorder/', TaskReorder.as_view(), name='task-reorder'),

    # Add default categories and tags (for testing or initial setup)
    path('add_default_data/', add_default_categories_tags, name='add_default_data'),
]
