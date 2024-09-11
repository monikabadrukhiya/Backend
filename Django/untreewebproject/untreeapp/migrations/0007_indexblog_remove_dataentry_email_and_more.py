# Generated by Django 5.0.7 on 2024-09-04 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('untreeapp', '0006_alter_dataentry_email_alter_dataentry_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Indexblog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Photo', models.ImageField(upload_to='image/')),
                ('Title', models.CharField(max_length=20)),
                ('Name', models.CharField(max_length=20)),
                ('Date', models.CharField(max_length=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='dataentry',
            name='Email',
        ),
        migrations.RemoveField(
            model_name='dataentry',
            name='Name',
        ),
    ]