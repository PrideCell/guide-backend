# Generated by Django 4.0.4 on 2023-03-22 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0055_alter_team_project_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='project_name',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='team',
            name='teamID',
            field=models.CharField(max_length=10),
        ),
    ]