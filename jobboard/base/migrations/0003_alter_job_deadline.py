# Generated by Django 5.0.6 on 2024-05-12 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_job_creator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='deadline',
            field=models.DateField(null=True),
        ),
    ]
