# Generated by Django 5.0.7 on 2024-09-13 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sessionapp', '0004_delete_login'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=50)),
                ('Email', models.CharField(max_length=50)),
                ('Password', models.CharField(max_length=50)),
                ('Reenterpassword', models.CharField(max_length=50)),
            ],
        ),
    ]
