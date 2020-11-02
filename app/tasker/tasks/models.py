from django.db import models
from django.urls import reverse


class TaskList(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Task List"
        verbose_name_plural = "Task Lists"

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self) -> str:
        return reverse("tasklist-detail", kwargs={"slug": self.slug})

    @property
    def done_items(self) -> models.QuerySet["TaskItem"]:
        return self.items.filter(is_done=True)

    @property
    def not_done_items(self) -> models.QuerySet["TaskItem"]:
        return self.items.filter(is_done=False)


class TaskItem(models.Model):
    task_list = models.ForeignKey(
        TaskList,
        related_name="items",
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=255)
    is_done = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Task Item"
        verbose_name_plural = "Task Items"

    def __str__(self) -> str:
        return self.name
