from django.shortcuts import render, get_object_or_404, redirect

from endpoints.forms import EditEndpointForm, DeleteEndpointForm, DetailsEndpointForm, CreateEndpointForm, \
    DetailsTagForm, EditTagForm, AddTag
from endpoints.models import Endpoint, Tag
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

def tags_list(request):
    tags = Tag.objects.all()

    context = {
        'tags': tags,
        'page_title': 'All Tags'
    }

    return render(request, 'tags/tags_list.html', context)

def tag_details(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    endpoint = tag.endpoint_set.all()

    context = {
        'tag': tag,
        'endpoint': endpoint,
        'page_title': f'{tag} Details'
    }

    return render(request, 'tags/tag_detail.html', context)

def edit_tag(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    form = EditTagForm(request.POST or None, instance=tag)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('endpoints:tag_details', pk=tag.pk)

    context = {
        'tag': tag,
        'form': form,
        'page_title': f'{tag} Edit'
    }

    return render(request, 'tags/tag_edit.html', context)

def add_tag(request):
    form = AddTag(request.POST or None)

    if request.method == "POST" and form.is_valid():
        tag = form.save()
        return redirect('endpoints:tag_details', pk=tag.pk)

    context = {
        'form': form,
        'page_title': 'Add Tag'
    }

    return render(request, 'tags/add_tag.html', context)
