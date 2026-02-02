from django.core.validators import RegexValidator

validate_version_format = RegexValidator(
    regex=r'^\d+\.\d+\.\d+$',
    message="Version must be in 'X.X.X' format (e.g., 1.0.0).",
    code='invalid_version'
)