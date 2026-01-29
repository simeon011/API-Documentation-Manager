from django.contrib import admin

from endpoints.models import Tag, Endpoint


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    ...

@admin.register(Endpoint)
class EndpointAdmin(admin.ModelAdmin):
    list_display = ['project', 'method', 'created_at']
    list_filter = ['method', 'project', 'tags']
    readonly_fields = ['created_at', 'updated_at']
