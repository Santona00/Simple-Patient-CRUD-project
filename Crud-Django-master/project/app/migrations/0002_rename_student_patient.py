# Generated by Django 4.1.6 on 2023-02-13 02:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Student',
            new_name='Patient',
        ),
    ]
