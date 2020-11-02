import json
from typing import Any, Dict

from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.views.generic import CreateView, DetailView, ListView
from todo.todos.forms import TodoListForm
from todo.todos.models import TodoList


class TodoListListView(ListView):
    template_name = "list.html"
    model = TodoList
    context_object_name = "todolists"

    def get_context_data(self, **kwargs: Dict[str, Any]) -> Dict[str, Any]:
        return super().get_context_data(form=TodoListForm(), **kwargs)


class TodoListCreateView(CreateView):
    template_name = "create.html"
    model = TodoList
    form_class = TodoListForm

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        todo_list = form.save()
        response = HttpResponse()
        response["HX-Trigger"] = json.dumps(
            {"redirect": {"url": todo_list.get_absolute_url()}}
        )
        return response


class TodoListDetailView(DetailView):
    template_name = "detail.html"
    model = TodoList
    context_object_name = "todolist"
