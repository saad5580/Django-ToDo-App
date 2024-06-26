from django.contrib import admin
from .models import Task
# Register your models here.
class TasksAdmin(admin.ModelAdmin):
    list_display = ('task', 'is_completed', 'updated_at')

admin.site.register(Task, TasksAdmin)
