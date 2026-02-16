from django import forms

from endpoints.models import Endpoint, Tag


class EndpointForm(forms.ModelForm):
    class Meta:
        model = Endpoint
        exclude = ('project',)
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
            'path': forms.TextInput(attrs={'class': 'form-control'}),
            'method': forms.Select(attrs={'class': 'form-select'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
class EditEndpointForm(EndpointForm):
    ...
class DeleteEndpointForm(EndpointForm):
    ...
class CreateEndpointForm(EndpointForm):
    ...

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'
class EditTagForm(TagForm):
    ...
class AddTag(TagForm):
    ...