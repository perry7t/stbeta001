# Generated by Django 4.1.5 on 2023-02-06 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shifts', '0003_status_status_name_status_style'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='style',
            field=models.TextField(blank=True, default='', verbose_name='style'),
        ),
    ]
