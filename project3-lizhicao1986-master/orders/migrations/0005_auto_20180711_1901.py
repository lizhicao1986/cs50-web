# Generated by Django 2.0.7 on 2018-07-11 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='pizza_order',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='pizza_orders', to='orders.pizza'),
        ),
        migrations.AlterField(
            model_name='order',
            name='sub_order',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_orders', to='orders.subs'),
        ),
    ]
