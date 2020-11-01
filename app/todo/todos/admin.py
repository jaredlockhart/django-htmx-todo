from django.contrib import admin

from todo.todos.models import TodoList, TodoItem

# Register your models here.
admin.site.register(TodoList)
admin.site.register(TodoItem)
