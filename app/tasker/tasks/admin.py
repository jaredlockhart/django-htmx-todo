from django.contrib import admin

from tasker.tasks.models import TaskList, TaskItem

# Register your models here.
admin.site.register(TaskList)
admin.site.register(TaskItem)
