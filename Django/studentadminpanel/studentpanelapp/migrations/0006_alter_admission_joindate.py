# Generated by Django 5.0.7 on 2024-09-30 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentpanelapp', '0005_admission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admission',
            name='Joindate',
            field=models.CharField(max_length=12),
        ),
    ]