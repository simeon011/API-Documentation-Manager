from django.contrib import admin
from django.urls import path, include

from common.views import dashboard

urlpatterns = [
    path('admin/', admin.site.urls),

    # Dashboard-ът става начална страница
    path('', dashboard, name='dashboard'),

    # Включваме проектите с namespace
    path('projects/', include('projects.urls', namespace='projects')),
    path('endpoints/', include('endpoints.urls', namespace='endpoints')),
]
handler404 = 'common.views.custom_404_view'
