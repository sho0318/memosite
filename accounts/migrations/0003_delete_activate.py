# Generated by Django 4.0.3 on 2022-05-07 02:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_activate'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Activate',
        ),
    ]