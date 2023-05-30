from django.urls import path
from . import views

urlpatterns = [
    # ADD A NEW TASK
    path('addTask/', views.addTask, name='addTask'),

    # MARK TASK AS DONE
    path('mark_as_done/<int:pk>/', views.mark_as_done, name='mark_as_done'),

    # MARK TASK AS UNDONE
    path('mark_as_undone/<int:pk>/', views.mark_as_undone, name='mark_as_undone'),

    # EDIT TASK
    path('edit_task/<int:pk>/', views.edit_task, name='edit_task'),

    #DELETE TASK
    path('delete_task/<int:pk>/', views.delete_task, name='delete_task'),



]