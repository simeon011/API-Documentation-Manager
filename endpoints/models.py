from django.db import models

from common.models import TimeStampedModel
from endpoints.validators import validate_start_slash
from projects.models import Project


class Tag(TimeStampedModel):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Endpoint(TimeStampedModel):

    class MethodChoices(models.TextChoices):
        GET = 'GET', 'GET'
        POST = 'POST', 'POST'
        PUT = 'PUT', 'PUT'
        DELETE = 'DELETE', 'DELETE'

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='endpoints')
    path = models.CharField(max_length=300, validators=[validate_start_slash], help_text="Example: /api/v1/users/")
    method = models.CharField(choices=MethodChoices.choices, max_length=50)
    description = models.TextField(blank=True, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f"[{self.method}] {self.path}"



