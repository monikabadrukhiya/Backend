# Generated by Django 5.0.7 on 2024-09-10 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('untreeapp', '0017_alter_cart_quantity_alter_cart_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='Total',
            field=models.IntegerField(default=1),
        ),
    ]
