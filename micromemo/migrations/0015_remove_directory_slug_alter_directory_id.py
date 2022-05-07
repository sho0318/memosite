# Generated by Django 4.0.3 on 2022-05-02 10:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('micromemo', '0014_directory_create_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='directory',
            name='slug',
        ),
        migrations.AlterField(
            model_name='directory',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
