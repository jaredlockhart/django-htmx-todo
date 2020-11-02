from django.urls import path
from tasker.tasks.views import (
    TaskListCreateView,
    TaskListDetailView,
    TaskListFilterView,
    TaskListListView,
)

urlpatterns = [
    path("filter/", TaskListFilterView.as_view(), name="tasklist-filter"),
    path("create/", TaskListCreateView.as_view(), name="tasklist-create"),
    path("<slug:slug>/", TaskListDetailView.as_view(), name="tasklist-detail"),
    path("", TaskListListView.as_view(), name="tasklist-list"),
]
