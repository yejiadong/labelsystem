# Generated by Django 3.2.15 on 2022-09-08 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='department',
            new_name='institution',
        ),
    ]
