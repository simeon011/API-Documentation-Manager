from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models
from common.models import TimeStampedModel
from projects.validators import validate_version_format, validate_base_url_format


class Project(TimeStampedModel):

    class choices_languages(models.TextChoices):
        PYTHON = 'Python', 'Python'
        JAVASCRIPT = 'Javascript', 'JavaScript'
        GO = 'Go', 'Go'
        JAVA = 'Java', 'Java'
        CSHARP = 'C#', 'C#'
        PHP = 'PHP', 'PHP'

    name = models.CharField(max_length=100, validators=[MinLengthValidator(3), MaxLengthValidator(100)])
    version = models.CharField(max_length=100, validators=[validate_version_format])
    base_url = models.URLField(validators=[validate_base_url_format])
    description = models.TextField()
    language = models.CharField(choices=choices_languages.choices, max_length=50)

    def __str__(self):
        return self.name


