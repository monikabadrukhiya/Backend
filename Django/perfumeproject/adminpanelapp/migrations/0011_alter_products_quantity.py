# Generated by Django 5.0.7 on 2024-11-18 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanelapp', '0010_products_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
