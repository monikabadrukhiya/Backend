# Generated by Django 5.0.7 on 2024-11-15 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfumeapp', '0006_delete_login'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
