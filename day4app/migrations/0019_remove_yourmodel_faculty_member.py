# Generated by Django 4.2.7 on 2024-05-16 19:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('day4app', '0018_rename_image_yourmodel_faculty_member'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='yourmodel',
            name='faculty_member',
        ),
    ]
