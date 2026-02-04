from django.urls import path, include

from endpoints.views import edit_endpoint, delete_endpoint, details_endpoint, add_endpoint
from projects.views import project_add

app_name = 'endpoints'

urlpatterns = [
    path('<int:pk>/', include([

        path('project/create/', add_endpoint, name='add_endpoint'),
        path('details/', details_endpoint, name='detail_endpoint'),
        path('edit/', edit_endpoint, name='edit_endpoint'),
        path('delete/', delete_endpoint, name='delete_endpoint'),
    ]))



]