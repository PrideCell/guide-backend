# Generated by Django 4.2 on 2023-07-28 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0010_alter_guide_myimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='app_video',
        ),
        migrations.RemoveField(
            model_name='team',
            name='product_video',
        ),
    ]