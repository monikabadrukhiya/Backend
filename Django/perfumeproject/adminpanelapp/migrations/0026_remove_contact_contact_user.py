# Generated by Django 5.0.7 on 2024-11-29 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanelapp', '0025_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='Contact_user',
        ),
    ]
