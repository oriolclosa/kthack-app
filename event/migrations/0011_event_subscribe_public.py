# Generated by Django 2.2.4 on 2019-08-08 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0010_event_companies_open'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='subscribe_public',
            field=models.BooleanField(default=True),
        ),
    ]
