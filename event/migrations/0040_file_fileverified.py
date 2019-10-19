# Generated by Django 2.2.4 on 2019-10-19 12:24

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0039_add_letter_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('file', models.FileField(upload_to='file')),
                ('type', models.PositiveSmallIntegerField(choices=[(0, 'INVOICE'), (1, 'LETTER')], default=0)),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'VALID'), (1, 'DEPRECATED'), (2, 'INVALID')], default=0)),
                ('verification_control', models.CharField(max_length=255)),
                ('verification_code', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='FileVerified',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('verified_at', models.DateTimeField(auto_now_add=True)),
                ('file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.File')),
            ],
        ),
    ]
