from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('login/', views.login, name='login'),
    path('index/', views.index, name='home'),
    path('list/', views.post_list, name='post_list'),
    path('sobre/', views.about, name='about'),
    path('contato/', views.contact, name='contact'),
    path('helloworld/', views.helloWorld),

    # Layouts
    path('stepper/', views.stepper, name='stepper'),
    path('list/', views.list, name='list'),
    path('infinite/', views.infiniteList, name='infinite_list'),
    path('accordion/', views.accordion, name='accordion'),
    path('tabs/', views.tabs, name='tabs'),

    # Forms
    path('forminputs/', views.formInputs, name='form_inputs'),
    path('formlayouts/', views.formLayouts, name='form_layouts'),
    path('buttons/', views.buttons, name='buttons'),
    path('datepicker/', views.datepicker, name='datepicker'),

    path('tasks/', views.taskList, name='task-list'),
    path('task/<int:id>', views.taskView, name="task-view"),
    path('newtask/', views.newTask, name="new-task"),
    path('changestatus/<int:id>', views.changeStatus, name="change-status"),
    path('edit/<int:id>', views.editTask, name="edit-task"),
    path('delete/<int:id>', views.deleteTask, name="delete-task"),
    path('yourname/<str:name>', views.yourName, name='your-name'),
]