# Generated by Django 3.1.4 on 2021-02-04 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0003_auto_20210202_0930'),
    ]

    operations = [
        migrations.CreateModel(
            name='product_tb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=20)),
                ('details', models.CharField(max_length=50)),
                ('catagory', models.CharField(max_length=20)),
                ('stock', models.CharField(max_length=20)),
                ('price', models.CharField(max_length=20)),
            ],
        ),
    ]
