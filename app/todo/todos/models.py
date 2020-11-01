from django.db import models


class TodoList(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Todo List"
        verbose_name_plural = "Todo Lists"

    def __str__(self):
        return self.name


class TodoItem(models.Model):
    todo_list = models.ForeignKey(TodoList, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    is_done = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Todo Item"
        verbose_name_plural = "Todo Items"

    def __str__(self):
        return self.name
