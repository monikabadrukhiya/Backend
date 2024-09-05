# Generated by Django 5.0.7 on 2024-09-04 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('untreeapp', '0012_shopdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aboutdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Photo', models.ImageField(upload_to='image/')),
                ('Name', models.CharField(max_length=50)),
                ('Position', models.CharField(max_length=10)),
                ('Description', models.CharField(max_length=200)),
                ('LM', models.CharField(max_length=200)),
            ],
        ),
    ]
