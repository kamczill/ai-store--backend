# Generated by Django 4.2.2 on 2023-07-17 21:16

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
                ('title', models.CharField(max_length=100, unique=True)),
                ('author', models.CharField(max_length=100)),
                ('description', models.CharField(unique=True)),
                ('cover', models.FileField(upload_to='files/')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('net_price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
    ]
