# Generated by Django 4.2.2 on 2023-07-20 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='tax',
            field=models.PositiveIntegerField(default=5),
        ),
    ]
