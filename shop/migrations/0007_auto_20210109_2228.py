# Generated by Django 3.1.3 on 2021-01-09 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_orderupdate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderupdate',
            name='order_desc',
        ),
        migrations.AddField(
            model_name='orderupdate',
            name='update_desc',
            field=models.CharField(default='', max_length=5000),
        ),
    ]
