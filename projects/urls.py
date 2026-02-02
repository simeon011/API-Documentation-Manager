from django.urls import path, include

from projects.views import project_list_view, project_details, project_edit, project_delete, project_add

app_name = 'projects'

urlpatterns = [
    path('', project_list_view, name='projects_list'),
    path('create/', project_add, name='project_add'),
    path('details/<int:pk>/', include([
        path('', project_details, name='project_details'),
        path('edit/', project_edit, name='project_edit'),
        path('delete/', project_delete, name='project_delete'),
    ])),
]