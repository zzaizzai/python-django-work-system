# Generated by Django 3.1.13 on 2023-01-01 05:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0006_member_team'),
        ('works', '0018_auto_20221230_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.team'),
        ),
    ]
