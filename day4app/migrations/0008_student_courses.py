# Generated by Django 4.2.8 on 2024-02-08 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('day4app', '0007_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='courses',
            field=models.ManyToManyField(to='day4app.course'),
        ),
    ]
