# Generated by Django 4.1.2 on 2022-10-26 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0002_rename_customer_reward_customers_reward_customer_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wallet',
            name='pin',
        ),
        migrations.AlterField(
            model_name='customer',
            name='profile_picture',
            field=models.ImageField(upload_to='profile_pictures/'),
        ),
    ]
