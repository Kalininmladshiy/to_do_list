from django.db import models
from django.utils import timezone

class TodoList(models.Model):
    title = models.CharField(verbose_name='задание', max_length=200)
    content = models.TextField(verbose_name='описание задания', blank=True)
    created = models.DateField(verbose_name='дата создания', auto_now_add=True)
    finished_date = models.DateField(verbose_name='сделать до', null=True, blank=True)
    file = models.FileField(verbose_name='файл', null=True)
    is_complete = models.BooleanField('завершено', null=True)
    class Meta:
        ordering = ["-finished_date"]
    def __str__(self):
        return self.title
