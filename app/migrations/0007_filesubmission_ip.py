# Generated by Django 2.2.4 on 2019-10-25 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("app", "0006_filesubmission")]

    operations = [
        migrations.AddField(
            model_name="filesubmission",
            name="ip",
            field=models.CharField(blank=True, max_length=255, null=True),
        )
    ]
