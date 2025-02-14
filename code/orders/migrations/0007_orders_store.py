# Generated by Django 4.2.13 on 2024-06-23 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0002_store_suppliers"),
        ("orders", "0006_alter_orders_lastedit"),
    ]

    operations = [
        migrations.AddField(
            model_name="orders",
            name="store",
            field=models.ForeignKey(
                default=-1,
                on_delete=django.db.models.deletion.CASCADE,
                to="store.store",
                verbose_name="Store",
            ),
            preserve_default=False,
        ),
    ]
