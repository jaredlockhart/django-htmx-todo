from typing import Any

from django import forms
from django.utils.text import slugify
from todo.todos.models import TodoList


class TodoListForm(forms.ModelForm):
    slug = forms.CharField(required=False, widget=forms.widgets.HiddenInput())

    class Meta:
        model = TodoList
        fields = ("name", "slug")

    def clean_name(self) -> str:
        name: str = self.cleaned_data["name"]
        slug = slugify(name)
        if TodoList.objects.filter(slug=slug).exists():
            raise forms.ValidationError(f"A To Do List with the name {name} exists")
        return name

    def save(self, commit: bool = True) -> Any:
        todo_list = super().save(commit)
        todo_list.slug = slugify(todo_list.name)
        todo_list.save()
        return todo_list
