# Generated by Django 3.0.3 on 2020-06-22 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='list',
            name='completed',
        ),
    ]