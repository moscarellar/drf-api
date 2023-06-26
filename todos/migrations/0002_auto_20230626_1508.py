# Generated by Django 3.2.16 on 2023-06-26 15:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'ordering': ['deadline']},
        ),
        migrations.AddField(
            model_name='todo',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 3, 15, 8, 23, 192898)),
        ),
        migrations.AddField(
            model_name='todo',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
