# Generated by Django 3.1.13 on 2022-12-27 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commissions', '0007_commissioncomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='commission',
            name='is_cancled',
            field=models.BooleanField(default=False),
        ),
    ]
