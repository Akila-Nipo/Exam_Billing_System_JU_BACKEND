# Generated by Django 4.2.7 on 2024-01-30 09:33

import day4app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('day4app', '0003_course_course_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_type',
            field=models.CharField(default='Theory', max_length=40, verbose_name=day4app.models.CourseType),
        ),
    ]