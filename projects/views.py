from django.shortcuts import render
from django.views.generic import ListView

from projects.models import Project


def project_list_view(request):
    # Ето я твоята команда!
    projects = Project.objects.all()

    context = {
        'projects': projects
    }

    return render(request, 'projects/project_list.html', context)
