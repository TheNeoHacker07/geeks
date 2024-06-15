

from django.urls import path
from .views import CreateTodo,ListTodo,RetrieveTodo,UpdateTodo,DeleteTodo


urlpatterns=[
    path('create_todo/',CreateTodo.as_view()),
    path('get_list_todo/',ListTodo.as_view()),
    path('get_retrieve_todo/<int:pk>/',RetrieveTodo.as_view()),
    path('delete_todo/<int:pk>/',DeleteTodo.as_view()),
    path('update_todo/<int:pk>/',UpdateTodo.as_view())
    
    
]