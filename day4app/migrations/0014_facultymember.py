# Generated by Django 4.2.7 on 2024-04-09 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('day4app', '0013_examcommittee_alter_rate_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacultyMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.URLField()),
                ('rank', models.CharField(choices=[('Professor', 'Professor'), ('Associate Professor', 'Associate Professor'), ('Assistant Professor', 'Assistant Professor'), ('Lecturer', 'Lecturer')], max_length=100)),
                ('bank_account_number', models.CharField(max_length=20)),
            ],
        ),
    ]
