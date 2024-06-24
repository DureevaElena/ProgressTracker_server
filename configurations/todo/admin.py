from django.contrib import admin

from .models import NoteTodo, StageNoteTodo


admin.site.register(NoteTodo)
admin.site.register(StageNoteTodo)