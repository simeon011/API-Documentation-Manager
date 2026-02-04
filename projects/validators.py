from django.core.validators import RegexValidator

validate_version_format = RegexValidator(
    regex=r'^(\d+\.\d+\.\d+|\d+\.\d+\.\d+\.\d+)$',
    message="Version must be in 'X.X.X' or 'X.X.X.X' format (e.g., 1.0.0).",
    code='invalid_version'
)

validate_base_url_format = RegexValidator(
    regex=r'^https:\/\/www\..+',
    message="Base URL must be in 'www.' format (e.g., http://).",
    code='invalid_base_url'
)