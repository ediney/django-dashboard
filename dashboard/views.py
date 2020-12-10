from django.contrib.auth.decorators import login_required
from django.core.checks import messages
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .forms import TaskForm
from .models import Task
import datetime


def login(request):
 return render(request, 'registration/login.html')


def index(request):
 return render(request, 'dashboard/index.html')


def post_list(request):
 return render(request, 'dashboard/post_list.html')


def about(request):
 return render(request, 'dashboard/about_us.html')


def contact(request):
 return render(request, 'dashboard/contact.html')


# Layout
def stepper(request):
 return render(request, 'dashboard/layout/stepper.html')


def list(request):
 return render(request, 'dashboard/layout/list.html')


def infiniteList(request):
 return render(request, 'dashboard/layout/infinite_lists.html')


def accordion(request):
 return render(request, 'dashboard/layout/accordion.html')


def tabs(request):
 return render(request, 'dashboard/layout/tabs.html')


# Forms
def formInputs(request):
 return render(request, 'dashboard/layout/form_inputs.html')


def formLayouts(request):
 return render(request, 'dashboard/layout/form_layouts.html')


def buttons(request):
 return render(request, 'dashboard/layout/buttons.html')


def datepicker(request):
 return render(request, 'dashboard/layout/datepicker.html')


@login_required
def taskList(request):
    search = request.GET.get('search')
    filter = request.GET.get('filter')
    tasksDoneRecently = Task.objects.filter(done='done', updated_at__gt=datetime.datetime.now() - datetime.timedelta(
        days=30)).count()
    tasksDone = Task.objects.filter(done='done', user=request.user).count()
    tasksDoing = Task.objects.filter(done='doing', user=request.user).count()

    if search:
        tasks = Task.objects.filter(title__icontains=search, user=request.user)
    elif filter:
        tasks = Task.objects.filter(done=filter, user=request.user)
    else:
        tasks_list = Task.objects.all().order_by('-created_at').filter(user=request.user)

        paginator = Paginator(tasks_list, 3)

        page = request.GET.get('page')
        tasks = paginator.get_page(page)

    return render(request, 'dashboard/tasks/buttons.html',
                  {'tasks': tasks, 'tasksrecently': tasksDoneRecently, 'tasksdone': tasksDone,
                   'tasksdoing': tasksDoing})


@login_required
def taskView(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, 'dashboard/tasks/task.html', {'task': task})


@login_required
def newTask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.done = 'doing'
            task.user = request.user
            task.save()
            return redirect('/')
    else:
        form = TaskForm()
        return render(request, 'dashboard/tasks/addtask.html', {'form': form})


@login_required
def editTask(request, id):
    task = get_object_or_404(Task, pk=id)
    form = TaskForm(instance=task)

    if (request.method == 'POST'):
        form = TaskForm(request.POST, instance=task)

        if (form.is_valid()):
            task.save()
            return redirect('/')
        else:
            return render(request, 'dashboard/task/edittask.html', {'form': form, 'task': task})
    else:
        return render(request, 'dashboard/tasks/edittask.html', {'form': form, 'task': task})


@login_required
def deleteTask(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()

    messages.info(request, 'Tarefa deletada com sucesso.')

    return redirect('/')


@login_required
def changeStatus(request, id):
    task = get_object_or_404(Task, pk=id)

    if (task.done == 'doing'):
        task.done = 'done'
    else:
        task.done = 'doing'

    task.save()

    return redirect('/')


def helloWorld(request):
    return HttpResponse('Hello World!')


@login_required
def yourName(request, name):
    return render(request, 'dashboard/tasks/yourname.html', {'name': name})