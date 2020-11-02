import json
from typing import Any, Dict

from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.views.generic import CreateView, DetailView, ListView
from tasker.tasks.forms import TaskListForm
from tasker.tasks.models import TaskList


class TaskListListView(ListView):
    template_name = "list.html"
    model = TaskList
    context_object_name = "tasklists"

    def get_context_data(self, **kwargs: Dict[str, Any]) -> Dict[str, Any]:
        return super().get_context_data(form=TaskListForm(), **kwargs)


class TaskListCreateView(CreateView):
    template_name = "create.html"
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
    template_name = "detail.html"
    model = TaskList
    context_object_name = "tasklist"
