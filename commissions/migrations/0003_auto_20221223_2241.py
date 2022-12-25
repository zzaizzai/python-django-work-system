# Generated by Django 3.1.13 on 2022-12-23 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0006_member_team'),
        ('commissions', '0002_auto_20221223_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commission',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='teams.team'),
        ),
    ]