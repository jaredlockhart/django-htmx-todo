import json
from typing import Any, Dict

from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.views.generic import CreateView, DetailView, ListView
from django_filters.views import FilterView
from tasker.tasks.filters import TaskListFilter
from tasker.tasks.forms import TaskListForm
from tasker.tasks.models import TaskList


class TaskListListView(ListView):
    model = TaskList

    def get_context_data(self, **kwargs: Dict[str, Any]) -> Dict[str, Any]:
        return super().get_context_data(form=TaskListForm(), **kwargs)


class TaskListFilterView(FilterView):
    filterset_class = TaskListFilter


class TaskListCreateView(CreateView):
    model = TaskList
    form_class = TaskListForm

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        task_list = form.save()
        response = HttpResponse()
        response["HX-Trigger"] = json.dumps(
            {"redirect": {"url": task_list.get_absolute_url()}}
        )
        return response


class TaskListDetailView(DetailView):
    model = TaskList
