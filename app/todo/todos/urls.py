from django.urls import path

from todo.todos.views import TodosListView

urlpatterns = [path("", TodosListView.as_view())]
