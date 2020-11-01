from django.views.generic import TemplateView


class TodosListView(TemplateView):
    template_name = "list.html"
