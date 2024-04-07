# Generated by Django 4.0.4 on 2022-07-13 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0019_alter_takeaway_order_alter_takeaway_total_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='tablereservation',
            name='reason_for_cancel',
            field=models.TextField(default='-', verbose_name='Причина скасування'),
        ),
        migrations.AddField(
            model_name='tablereservation',
            name='status',
            field=models.CharField(default='Новe', max_length=128, verbose_name='Статус'),
        ),
        migrations.AddField(
            model_name='tablereservation',
            name='visible_for_admin',
            field=models.BooleanField(default=True, verbose_name='Видно для адміну'),
        ),
        migrations.AddField(
            model_name='takeaway',
            name='reason_for_cancel',
            field=models.TextField(default='-', verbose_name='Причина скасування'),
        ),
        migrations.AddField(
            model_name='takeaway',
            name='status',
            field=models.CharField(default='Новe', max_length=128, verbose_name='Статус'),
        ),
        migrations.AddField(
            model_name='takeaway',
            name='visible_for_admin',
            field=models.BooleanField(default=True, verbose_name='Видно для адміну'),
        ),
    ]
