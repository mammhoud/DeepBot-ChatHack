# Generated by Django 4.0.10 on 2023-12-13 21:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_remove_customer_business_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='email',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='name',
        ),
    ]
