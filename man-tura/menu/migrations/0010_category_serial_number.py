# Generated by Django 4.0.4 on 2022-07-28 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0009_remove_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='serial_number',
            field=models.IntegerField(default=0),
        ),
    ]
