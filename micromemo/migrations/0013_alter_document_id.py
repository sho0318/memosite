# Generated by Django 4.0.3 on 2022-05-02 08:00

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('micromemo', '0012_remove_comment_post_delete_account_delete_comment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
