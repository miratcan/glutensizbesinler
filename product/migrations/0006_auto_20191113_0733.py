# Generated by Django 2.2.7 on 2019-11-13 07:33

from django.db import migrations
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20191111_1131'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supplier',
            name='address',
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='description',
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='google_place_id',
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='supplier',
            name='data',
            field=django_mysql.models.JSONField(blank=True, default=dict, null=True),
        ),
    ]
