# Generated by Django 2.2 on 2021-08-29 04:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0003_customer_vehicle'),
    ]

    operations = [
        migrations.DeleteModel(
            name='customer_vehicle',
        ),
    ]