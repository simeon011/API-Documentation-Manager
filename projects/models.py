from django.db import models
from common.models import TimeStampedModel

class Project(TimeStampedModel):

    class choices_languages(models.TextChoices):
        PYTHON = 'Python', 'Python'
        JAVASCRIPT = 'Javascript', 'Javascript'
        GO = 'Go', 'Go'
        JAVA = 'Java', 'Java'
        CSHARP = 'C#', 'C#'
        PHP = 'PHP', 'PHP'

    name = models.CharField(max_length=100)
    version = models.CharField(max_length=100)
    base_url = models.URLField()
    description = models.TextField()
    language = models.CharField(choices=choices_languages.choices, max_length=50)

    def __str__(self):
        return self.name


