# Generated by Django 2.2.4 on 2019-08-11 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0015_invoice'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='code_invoice_company',
            field=models.CharField(blank=True, max_length=31, null=True),
        ),
    ]
