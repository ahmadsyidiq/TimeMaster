# Generated by Django 4.2.7 on 2023-12-09 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeapp', '0004_rename_name_user_project_creators'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date_created',
            field=models.DateField(blank=True, null=True),
        ),
    ]