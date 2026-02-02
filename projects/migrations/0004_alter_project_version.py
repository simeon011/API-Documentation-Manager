import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_alter_project_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='version',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(code='invalid_version', message="Version must be in 'X.X.X' format (e.g., 1.0.0).", regex='^\\d+\\.\\d+\\.\\d+$')]),
        ),
    ]
