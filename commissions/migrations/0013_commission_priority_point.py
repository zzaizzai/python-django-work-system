# Generated by Django 3.1.13 on 2023-01-01 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commissions', '0012_auto_20230101_1405'),
    ]

    operations = [
        migrations.AddField(
            model_name='commission',
            name='priority_point',
            field=models.IntegerField(default=1),
        ),
    ]