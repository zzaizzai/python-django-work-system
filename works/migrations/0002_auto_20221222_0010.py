# Generated by Django 3.1.13 on 2022-12-21 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='work',
            name='timedate_created',
        ),
        migrations.AddField(
            model_name='work',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='work',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='work',
            name='datetime_completed',
            field=models.DateTimeField(null=True, verbose_name='completed datetime'),
        ),
        migrations.AlterField(
            model_name='work',
            name='department_charge',
            field=models.IntegerField(default=1, verbose_name='department in charger'),
        ),
        migrations.AlterField(
            model_name='work',
            name='description',
            field=models.CharField(max_length=255, null=True, verbose_name='Work description'),
        ),
    ]
