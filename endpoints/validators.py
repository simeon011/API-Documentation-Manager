from django.core.exceptions import ValidationError


def validate_start_slash(value):
    if not value.startswith('/'):
        raise ValidationError('The path must start with "/"')
