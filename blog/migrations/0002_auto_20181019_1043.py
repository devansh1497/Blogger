# Generated by Django 2.1.2 on 2018-10-19 10:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 19, 10, 43, 39, 746462, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
