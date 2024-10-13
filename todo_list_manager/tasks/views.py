from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def task_list(request):
    category = request.GET.get('category')
    if category:
        tasks = Task.objects.filter(category=category)
    else:
        tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')
        category = request.POST.get('category')
        priority = request.POST.get('priority')
        task = Task(title=title, description=description, due_date=due_date, category=category, priority=priority)
        task.save()
        return redirect('task_list')
    return render(request, 'tasks/add_task.html')

def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    
    if request.method == "POST":
        if request.POST.get('action') == 'update':
            # Update Task
            task.title = request.POST.get('title')
            task.description = request.POST.get('description')
            task.due_date = request.POST.get('due_date')
            task.completed = 'completed' in request.POST
            task.category = request.POST.get('category')
            task.priority = request.POST.get('priority')
            task.save()
            return redirect('task_list')

        elif request.POST.get('action') == 'delete':
            # Delete Task
            task.delete()
            return redirect('task_list')

    return render(request, 'tasks/update_task.html', {'task': task})
