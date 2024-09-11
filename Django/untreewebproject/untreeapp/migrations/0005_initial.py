# Generated by Django 5.0.7 on 2024-09-03 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('untreeapp', '0004_delete_dataentry'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dataentry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Photo', models.ImageField(upload_to='image/')),
                ('Product', models.CharField(max_length=20)),
                ('Price', models.CharField(max_length=10)),
                ('Name', models.CharField(max_length=20)),
                ('Email', models.CharField(max_length=20)),
            ],
        ),
    ]