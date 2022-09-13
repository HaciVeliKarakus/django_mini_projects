from django.contrib import admin

from apps.todo.models import Todo


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    ...
