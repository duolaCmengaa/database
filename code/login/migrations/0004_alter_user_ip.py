# Generated by Django 3.2.3 on 2021-06-04 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20210604_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='ip',
            field=models.CharField(default=0, max_length=40, verbose_name='Login ip'),
        ),
    ]
