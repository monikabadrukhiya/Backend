# Generated by Django 5.0.7 on 2024-09-04 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('untreeapp', '0010_indexblog'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserEnter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.CharField(max_length=50)),
                ('Name', models.CharField(max_length=50)),
            ],
        ),
    ]
