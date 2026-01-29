from django.urls import path

from projects.views import project_list_view

app_name = 'projects'

urlpatterns = [
    path('', project_list_view, name='projects_list')
]