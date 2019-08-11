# Generated by Django 2.2.4 on 2019-08-11 15:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('event', '0018_invoice_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='sent_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='sent_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
