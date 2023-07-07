# Generated by Django 4.2.2 on 2023-07-07 15:19

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('description', models.CharField()),
                ('cover', models.CharField()),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
