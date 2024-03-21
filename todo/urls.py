from django.urls import path
from .import views
from .views import ListTodo, DetailTodo


urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_todo, name='add'),
    path('complete/<todo_id>/', views.complete_todo, name='complete'),
    path('deletecompleted/', views.delete_completed, name='delete_completed'),
    path('deleteall/', views.delete_all, name='delete_all'),

    # API:
    path('api/', ListTodo.as_view(), name='todo_list'),
    path('api/<int:pk>/', DetailTodo.as_view(), name='todo_detail'),
]
