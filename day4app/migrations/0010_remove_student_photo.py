# Generated by Django 5.0.2 on 2024-02-13 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('day4app', '0009_student_photo_alter_student_stu_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='photo',
        ),
    ]