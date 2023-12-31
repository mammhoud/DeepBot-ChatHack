# Generated by Django 4.0.10 on 2023-12-22 22:34

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0004_remove_inventory_price'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HistoricalPtoduct_Type',
            new_name='HistoricalPtoducts_Type',
        ),
        migrations.RenameModel(
            old_name='Ptoduct_Type',
            new_name='Ptoducts_Type',
        ),
        migrations.AlterModelOptions(
            name='historicalptoducts_type',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical ptoducts_ type', 'verbose_name_plural': 'historical ptoducts_ types'},
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AlterField(
            model_name='inventory',
            name='description',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='is_active',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='is_featured',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='type',
            field=models.CharField(choices=[('T-Shirt', 'T-Shirt'), ('Shirt', 'Shirt'), ('Pants', 'Pants'), ('Shoes', 'Shoes')], default='T-Shirt', max_length=100),
        ),
    ]
