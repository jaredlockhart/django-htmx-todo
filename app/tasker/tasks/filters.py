import django_filters
from tasker.tasks.models import TaskList


class TaskListFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = TaskList
        fields = [
            "name",
        ]
