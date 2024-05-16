# Generated by Django 4.2.7 on 2024-05-16 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('day4app', '0015_yourmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('semester', models.CharField(max_length=20)),
                ('courses', models.TextField()),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]