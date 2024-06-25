from django.contrib import admin

from .models import NoteTodo, StageNoteTodo, CategoryTodo, StatusTodo, DoneTodo


admin.site.register(NoteTodo)
admin.site.register(StageNoteTodo)
admin.site.register(CategoryTodo)
admin.site.register(StatusTodo)
admin.site.register(DoneTodo)