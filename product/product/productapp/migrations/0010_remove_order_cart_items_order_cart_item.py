# Generated by Django 4.2.4 on 2024-12-05 09:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0009_remove_order_cart_items_order_cart_items'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='cart_items',
        ),
        migrations.AddField(
            model_name='order',
            name='cart_item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='productapp.cart'),
        ),
    ]
