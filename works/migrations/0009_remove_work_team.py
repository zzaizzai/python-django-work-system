# Generated by Django 3.1.13 on 2022-12-22 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0008_auto_20221222_2242'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='work',
            name='team_id',
        ),
    ]
