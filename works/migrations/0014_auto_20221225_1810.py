# Generated by Django 3.1.13 on 2022-12-25 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0013_auto_20221224_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='description',
            field=models.CharField(max_length=10000, null=True, verbose_name='Work description'),
        ),
    ]
