# Generated by Django 3.1.13 on 2022-12-25 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commissions', '0005_auto_20221224_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commission',
            name='description',
            field=models.CharField(blank=True, max_length=10000, null=True, verbose_name='description'),
        ),
    ]