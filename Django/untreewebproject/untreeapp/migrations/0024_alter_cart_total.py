# Generated by Django 5.0.7 on 2024-09-11 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('untreeapp', '0023_alter_cart_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='Total',
            field=models.IntegerField(default=0),
        ),
    ]