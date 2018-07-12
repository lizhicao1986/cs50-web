# Generated by Django 2.0.7 on 2018-07-11 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pizzaType', models.CharField(choices=[('RG', 'Regular'), ('SC', 'Sicilian')], default='RG', max_length=2)),
                ('size', models.CharField(choices=[('SM', 'Small'), ('LG', 'Large')], default='SM', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='subs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(choices=[('SM', 'Small'), ('LG', 'Large')], default='SM', max_length=2)),
                ('subType', models.CharField(choices=[('CH', 'Cheese'), ('IT', 'Italian')], default='CH', max_length=2)),
            ],
        ),
    ]