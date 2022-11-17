from django.contrib import admin

from .models import TodoList


@admin.register(TodoList)
class TodoListAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ('title', 'content', 'finished_date')
    list_filter = ('finished_date', 'created', 'is_complete')
