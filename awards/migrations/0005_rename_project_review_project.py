# Generated by Django 4.0.3 on 2022-03-14 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0004_alter_project_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='Project',
            new_name='project',
        ),
    ]