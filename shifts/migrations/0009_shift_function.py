# Generated by Django 4.1.5 on 2023-02-13 19:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shifts', '0008_customer_customer_short'),
    ]

    operations = [
        migrations.AddField(
            model_name='shift',
            name='function',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='shifts.function'),
        ),
    ]
