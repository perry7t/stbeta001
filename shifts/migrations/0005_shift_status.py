# Generated by Django 4.1.5 on 2023-02-06 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shifts', '0004_alter_status_style'),
    ]

    operations = [
        migrations.AddField(
            model_name='shift',
            name='status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='shifts.status'),
        ),
    ]
