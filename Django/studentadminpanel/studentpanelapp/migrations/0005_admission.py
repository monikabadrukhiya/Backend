# Generated by Django 5.0.7 on 2024-09-30 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentpanelapp', '0004_delete_admission'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Number', models.IntegerField(max_length=20)),
                ('Pnumber', models.IntegerField(max_length=20)),
                ('Study', models.CharField(max_length=50)),
                ('Cource', models.CharField(max_length=50)),
                ('Fees', models.CharField(max_length=50)),
                ('Duration', models.CharField(max_length=50)),
                ('Joindate', models.DateField(max_length=50)),
                ('Reference', models.CharField(max_length=50)),
                ('Photo', models.ImageField(upload_to=None)),
            ],
        ),
    ]
