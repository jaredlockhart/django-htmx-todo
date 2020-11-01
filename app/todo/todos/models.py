from django.db import models
from django.urls import reverse


class TodoList(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Todo List"
        verbose_name_plural = "Todo Lists"

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self) -> str:
        return reverse("todolist-detail", kwargs={"slug": self.slug})

    @property
    def done_items(self) -> models.QuerySet["TodoItem"]:
        return self.items.filter(is_done=True)

    @property
    def not_done_items(self) -> models.QuerySet["TodoItem"]:
        return self.items.filter(is_done=False)


class TodoItem(models.Model):
    todo_list = models.ForeignKey(
        TodoList,
        related_name="items",
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=255)
    is_done = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Todo Item"
        verbose_name_plural = "Todo Items"

    def __str__(self) -> str:
        return self.name
