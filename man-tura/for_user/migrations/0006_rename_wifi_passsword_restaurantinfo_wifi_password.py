# Generated by Django 4.0.4 on 2022-08-04 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('for_user', '0005_restaurantinfo_about_restaurant_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurantinfo',
            old_name='wifi_passsword',
            new_name='wifi_password',
        ),
    ]
