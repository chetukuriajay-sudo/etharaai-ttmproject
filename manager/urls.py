from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('projects/', views.projects_view, name='projects'),
    path('tasks/', views.tasks_view, name='tasks'),
    path('delete-task/<int:task_id>/', views.delete_task, name='delete_task'),
    path('delete-project/<int:project_id>/', views.delete_project, name='delete_project'),
    path('delete-account/', views.delete_account, name='delete_account'),
    path('edit-task/<int:task_id>/', views.edit_task, name='edit_task'),
    path('edit-project/<int:project_id>/', views.edit_project, name='edit_project'),
]
