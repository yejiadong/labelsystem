# Generated by Django 3.2 on 2023-01-24 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0016_auto_20221117_0650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annotation',
            name='general_label',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='annotation',
            name='overall_label',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='annotation',
            name='temporal_label',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]