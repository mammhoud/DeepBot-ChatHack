# Generated by Django 4.0.10 on 2023-12-10 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_rename_user_data_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='full_name',
            field=models.CharField(default='new user', max_length=100),
        ),
    ]
