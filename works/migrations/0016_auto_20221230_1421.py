# Generated by Django 3.1.13 on 2022-12-30 05:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('works', '0015_workcomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workcomment',
            name='description',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Work description'),
        ),
        migrations.CreateModel(
            name='WrokHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('kind', models.CharField(max_length=100, verbose_name='view, edit, cancle')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('parent_work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='works.work')),
            ],
        ),
    ]
