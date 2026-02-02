from django.contrib import admin

from projects.models import Project


@admin.register(Project)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ['name', 'language', 'version']
    readonly_fields = ['created_at', 'updated_at']
