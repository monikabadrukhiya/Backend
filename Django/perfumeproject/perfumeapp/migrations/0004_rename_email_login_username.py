# Generated by Django 5.0.7 on 2024-11-14 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfumeapp', '0003_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='login',
            old_name='email',
            new_name='username',
        ),
    ]
