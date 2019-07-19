# Generated by Django 2.2.3 on 2019-07-19 08:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=31, unique=True)),
                ('html_content', models.TextField()),
                ('published', models.BooleanField(default=False)),
            ],
        ),
    ]
