# Generated by Django 3.1.4 on 2021-01-29 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='register_tb',
            name='status',
            field=models.CharField(default='pending', max_length=20),
        ),
    ]
