# Generated by Django 3.2.3 on 2021-06-17 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='price',
            field=models.DecimalField(decimal_places=10, max_digits=10),
        ),
        migrations.AlterField(
            model_name='books',
            name='price_vip',
            field=models.DecimalField(decimal_places=10, max_digits=10),
        ),
    ]
