from django.db.models import Count
from django.shortcuts import render

from django.shortcuts import render

from endpoints.models import Endpoint
from projects.models import Project


def custom_404_view(request, exception):
    return render(request, '404.html', status=404)


def dashboard(request):
    sum_projects = Project.objects.count()
    sum_endpoints = Endpoint.objects.count()
    latest_projects = Project.objects.annotate(endpoints_count=Count('endpoints')).order_by('-updated_at')[:3]

    context = {
        'sum_projects': sum_projects,
        'sum_endpoints': sum_endpoints,
        'latest_projects': latest_projects,
        'page_title': 'Dashboard',
    }

    return render(request, 'common/dashboard.html', context)
