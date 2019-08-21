# Generated by Django 2.2.4 on 2019-08-21 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("event", "0022_add_event_type")]

    operations = [
        migrations.AlterField(
            model_name="companyevent",
            name="tier",
            field=models.PositiveSmallIntegerField(
                choices=[
                    (10, "TERA"),
                    (20, "GIGA"),
                    (30, "MEGA"),
                    (40, "KILO"),
                    (50, "MILI"),
                    (60, "PARTNER"),
                    (70, "SUPPORT"),
                    (80, "ORGANISER"),
                ]
            ),
        )
    ]