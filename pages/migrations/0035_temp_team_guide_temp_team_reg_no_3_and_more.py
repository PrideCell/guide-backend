# Generated by Django 4.0.4 on 2022-10-24 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0034_remove_temp_team_guide_remove_temp_team_reg_no_3_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='temp_team',
            name='guide',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='temp_team',
            name='reg_no_3',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='temp_team',
            name='student_3_email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='temp_team',
            name='student_3_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='temp_team',
            name='student_3_no',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
