from django import forms
from projects.validators import validate_version_format

from projects.models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'


class ProjectEditForm(ProjectForm):
    ...


class ProjectDeleteForm(ProjectForm):
    ...


class ProjectCreateForm(ProjectForm):
    name = forms.CharField(
        min_length=3,
        max_length=100,
    )
    # Добави валидатора тук, за да работи синхронно с модела
    version = forms.CharField(validators=[validate_version_format])

    class Meta:
        model = Project
        fields = '__all__'
        error_messages = {
            'name': {
                'required': "Project name is required.",
                'min_length': "The name is too short! It must be at least 3 characters.",
                'max_length': "The name is too long!",
            },
            'base_url': {
                'invalid': "Base URL must start with 'https://www.'",
            }

        }
