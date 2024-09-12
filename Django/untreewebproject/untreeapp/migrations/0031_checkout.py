# Generated by Django 5.0.7 on 2024-09-12 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('untreeapp', '0030_delete_checkout'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Country', models.CharField(max_length=20)),
                ('FName', models.CharField(max_length=50)),
                ('LName', models.CharField(max_length=50)),
                ('Company', models.CharField(max_length=50)),
                ('Address', models.CharField(max_length=50)),
                ('State', models.CharField(max_length=50)),
                ('Zip', models.IntegerField(max_length=50)),
                ('Email', models.CharField(max_length=50)),
                ('Phone', models.IntegerField(max_length=50)),
                ('Note', models.CharField(max_length=200)),
                ('CouponCode', models.IntegerField(max_length=50)),
                ('Password', models.CharField(max_length=20)),
            ],
        ),
    ]
