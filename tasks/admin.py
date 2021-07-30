from django.contrib import admin
from tasks.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title', 'deadline', 'date_created',
        'date_modified', 'done'
    ]
    list_editable = [
        'title'
    ]
    list_display_links = [
        'deadline', 'id'
    ]
    list_filter = [
        'date_created', 'date_modified', 'deadline', 'done'
    ]
    search_fields = [
        'title', 'description'
    ]