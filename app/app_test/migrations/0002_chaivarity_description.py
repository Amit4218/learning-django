# Generated by Django 5.2.2 on 2025-06-08 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_test', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chaivarity',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
