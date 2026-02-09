from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from projects.forms import ProjectEditForm, ProjectDeleteForm, ProjectCreateForm
from projects.models import Project


def project_list_view(request):
    projects = Project.objects.prefetch_related('endpoints').all()
    query = request.GET.get('q')
    if query:
        projects = projects.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(language__icontains=query)
        )

    context = {
        'projects': projects,
        'page_title': 'All Projects',
        'query': query
    }

    return render(request, 'projects/project_list.html', context)


def project_details(request, pk):
    project = get_object_or_404(Project, pk=pk)

    context = {
        'project': project,
        'page_title': f'{project.name} details'
    }

    return render(request, 'projects/details.html', context)

def project_edit(request, pk):
    project = get_object_or_404(Project, pk=pk)
    form = ProjectEditForm(request.POST or None, instance=project)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('projects:project_details', pk=project.pk)

    context = {
        'form': form,
        'project': project,
        'page_title': f'{project.name} edit'
    }

    return render(request, 'projects/edit_project.html', context)


def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    form = ProjectDeleteForm(request.POST or None, instance=project)

    if request.method == 'POST':
        project.delete()
        return redirect('projects:projects_list')

    context = {
        'form': form,
        'project': project,
        'page_title': f'{project.name} delete'
    }

    return render(request, 'projects/delete_project.html', context)


def project_add(request):
    form = ProjectCreateForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        project = form.save()
        return redirect('projects:project_details', pk=project.pk)

    context = {
        'form': form,
        'page_title': 'Add Project'
    }

    return render(request, 'projects/create_project.html', context)

