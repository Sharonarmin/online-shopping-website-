# Generated by Django 3.1.4 on 2021-02-04 05:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0005_auto_20210204_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_tb',
            name='seller',
            field=models.ForeignKey(default=9, on_delete=django.db.models.deletion.CASCADE, to='seller.register_tb1'),
        ),
    ]
