# Generated by Django 3.2.3 on 2021-06-17 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_auto_20210617_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='title',
            field=models.CharField(max_length=64, verbose_name='书名'),
        ),
    ]
