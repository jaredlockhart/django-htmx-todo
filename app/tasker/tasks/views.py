import json
from typing import Any, Dict, List, cast

from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.http.request import HttpRequest
from django.views.generic import CreateView, DetailView, ListView
from django_filters.views import FilterView
from tasker.tasks.filters import TaskListFilter
from tasker.tasks.forms import TaskListCreateForm
from tasker.tasks.models import TaskList


class TaskListListView(ListView):
    model = TaskList

    def get_context_data(self, **kwargs: Dict[str, Any]) -> Dict[str, Any]:
        return super().get_context_data(
            form=TaskListCreateForm(), filterset=TaskListFilter, **kwargs
        )


class TaskListFilterView(FilterView):
    filterset_class = TaskListFilter


class TaskListCreateView(CreateView):
    model = TaskList
    form_class = TaskListCreateForm
    template_name = "tasks/tasklist_create_form.html"

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        task_list = form.save()
        response = HttpResponse()
        response["HX-Trigger"] = json.dumps(
            {"redirect": {"url": task_list.get_absolute_url()}}
        )
        return response


class TaskListDetailView(DetailView):
    model = TaskList


class TaskListTasksView(DetailView):
    model = TaskList


class TaskListAddTaskView(DetailView):
    model = TaskList
    template_name = "tasks/tasklist_tasks.html"

    def post(
        self, request: HttpRequest, *args: List[Any], **kwargs: Dict[str, Any]
    ) -> HttpResponse:
        cast(TaskList, self.get_object()).tasks.create()
        return self.get(request, *args, **kwargs)
