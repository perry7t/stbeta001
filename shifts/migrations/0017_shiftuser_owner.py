# Generated by Django 4.1.5 on 2023-02-17 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shifts', '0016_alter_shift_end_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='shiftuser',
            name='owner',
            field=models.IntegerField(default=1),
        ),
    ]
