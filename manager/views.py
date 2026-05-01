from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib import messages

from .models import Project, Task
from .forms import SignupForm, ProjectForm, TaskForm


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})


def login_view(request):
    error = ''

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            error = 'Invalid username or password'

    return render(request, 'login.html', {'error': error})


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def dashboard(request):
    projects = Project.objects.filter(members=request.user) | Project.objects.filter(created_by=request.user)
    tasks = Task.objects.filter(project__in=projects).distinct()

    total_tasks = tasks.count()
    completed = tasks.filter(status='Completed').count()
    pending = tasks.filter(status='Pending').count()
    overdue = tasks.filter(due_date__lt=timezone.now().date()).exclude(status='Completed').count()

    progress = int((completed / total_tasks) * 100) if total_tasks > 0 else 0

    return render(request, 'dashboard.html', {
        'total_tasks': total_tasks,
        'completed': completed,
        'pending': pending,
        'overdue': overdue,
        'progress': progress,
        'tasks': tasks
    })


@login_required
def projects_view(request):
    projects = Project.objects.filter(members=request.user) | Project.objects.filter(created_by=request.user)

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.created_by = request.user
            project.save()
            form.save_m2m()
            project.members.add(request.user)
            messages.success(request, "Project created successfully")
            return redirect('projects')
    else:
        form = ProjectForm()

    return render(request, 'projects.html', {
        'projects': projects.distinct(),
        'form': form
    })


@login_required
def tasks_view(request):
    projects = Project.objects.filter(members=request.user) | Project.objects.filter(created_by=request.user)
    tasks = Task.objects.filter(project__in=projects).distinct()

    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            selected_project = form.cleaned_data['project']

            if selected_project.created_by == request.user:
                form.save()
                messages.success(request, "Task created successfully")
            else:
                messages.error(request, "Only project admin can create tasks.")

            return redirect('tasks')
    else:
        form = TaskForm()

    return render(request, 'tasks.html', {
        'tasks': tasks,
        'form': form
    })


@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.user == task.project.created_by:
        task.delete()
        messages.success(request, "Task deleted successfully")

    return redirect('tasks')


@login_required
def delete_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    if request.user == project.created_by:
        project.delete()
        messages.success(request, "Project deleted successfully")

    return redirect('projects')


@login_required
def delete_account(request):
    if request.method == 'POST':
        user = request.user

        for project in Project.objects.filter(members=user):
            project.members.remove(user)

        messages.success(request, "Account deleted successfully")
        user.delete()
        return redirect('login')

    return render(request, 'delete_account.html')


@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.user == task.project.created_by:
        if request.method == 'POST':
            form = TaskForm(request.POST, instance=task)
            if form.is_valid():
                form.save()
                messages.success(request, "Task updated successfully")
                return redirect('tasks')
        else:
            form = TaskForm(instance=task)

        return render(request, 'edit_task.html', {
            'form': form,
            'task': task,
            'role': 'admin'
        })

    if request.user == task.assigned_to:
        if request.method == 'POST':
            task.status = request.POST.get('status')
            task.save()
            messages.success(request, "Task status updated successfully")
            return redirect('tasks')

        return render(request, 'edit_task.html', {
            'task': task,
            'role': 'member'
        })

    return redirect('tasks')


@login_required
def edit_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    if request.user != project.created_by:
        return redirect('projects')

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, "Project updated successfully")
            return redirect('projects')
    else:
        form = ProjectForm(instance=project)

    return render(request, 'edit_project.html', {
        'form': form,
        'project': project
    })
