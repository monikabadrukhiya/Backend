# Generated by Django 5.0.7 on 2024-09-04 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('untreeapp', '0009_delete_indexblog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Indexblog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Photo', models.ImageField(upload_to='image/')),
                ('Title', models.CharField(max_length=50)),
                ('Name', models.CharField(max_length=20)),
                ('Date', models.CharField(max_length=20)),
            ],
        ),
    ]