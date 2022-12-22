# Generated by Django 3.1.13 on 2022-12-22 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0006_member_team'),
        ('works', '0009_remove_work_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='team_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='teams.team'),
        ),
    ]
