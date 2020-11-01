from django.urls import path
from todo.todos.views import TodoListCreateView, TodoListDetailView, TodoListListView

urlpatterns = [
    path("create/", TodoListCreateView.as_view(), name="todolist-create"),
    path("<slug:slug>/", TodoListDetailView.as_view(), name="todolist-detail"),
    path("", TodoListListView.as_view(), name="todolist-list"),
]
