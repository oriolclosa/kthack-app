# Generated by Django 2.2.4 on 2019-08-25 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0025_application_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='note',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
