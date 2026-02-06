from django.shortcuts import render, get_object_or_404, redirect

from endpoints.forms import EditEndpointForm, DeleteEndpointForm, DetailsEndpointForm, CreateEndpointForm
from endpoints.models import Endpoint
from projects.models import Project


def details_endpoint(request, pk):
    endpoint = get_object_or_404(Endpoint, pk=pk)

    context = {
        'endpoint': endpoint,
        'project': endpoint.project,
    }

    return render(request, 'endpoints/details_endpoint.html', context)


def edit_endpoint(request, pk):
    endpoint = get_object_or_404(Endpoint, pk=pk)
    form = EditEndpointForm(request.POST or None, instance=endpoint)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('projects:project_details', pk=endpoint.project.pk)

    context = {
        'endpoint': endpoint,
        'project': endpoint.project,
        'form': form,
        'page_title': f'{endpoint.project} Edit'
    }

    return render(request, 'endpoints/edit_endpoints.html', context)

    return render(request, 'endpoints/edit_endpoints.html', context)


def delete_endpoint(request, pk):
    endpoint = get_object_or_404(Endpoint, pk=pk)
    form = DeleteEndpointForm(request.POST or None, instance=endpoint)
    if request.method == 'POST':
        endpoint.delete()
        return redirect('projects:project_details', pk=endpoint.project.pk)

    context = {
        'endpoint': endpoint,
        'project': endpoint.project,
        'form': form,
        'page_title': f'{endpoint.project} Delete'
    }

    return render(request, 'endpoints/delete_endpoint.html', context)


def add_endpoint(request, pk):
    project = get_object_or_404(Project, pk=pk)
    form = CreateEndpointForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        endpoint = form.save(commit=False)
        endpoint.project = project
        endpoint.save()
        form.save_m2m()
        return redirect('projects:project_details', pk=project.pk)

    context = {
        'form': form,
        'project': project,
        'page_title': 'Create Endpoint'
    }

    return render(request, 'endpoints/create_endpoint.html', context)
