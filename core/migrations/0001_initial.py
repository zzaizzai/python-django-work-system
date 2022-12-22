# Generated by Django 3.1.13 on 2022-12-22 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('works', '0007_remove_work_workers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='commission title')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.IntegerField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('date_due', models.DateField(verbose_name='Work due')),
                ('team', models.IntegerField(default=1, verbose_name='department in charger')),
                ('datetime_completed', models.DateTimeField(blank=True, null=True, verbose_name='completed datetime')),
                ('user_completed', models.IntegerField(blank=True, null=True, verbose_name='completed user')),
                ('work_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='works.work')),
            ],
        ),
    ]
