# Generated by Django 4.0.6 on 2022-08-30 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reward',
            old_name='customer',
            new_name='customers',
        ),
        migrations.AddField(
            model_name='reward',
            name='customer_id',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='reward',
            name='name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='reward',
            name='gender',
            field=models.CharField(max_length=25, null=True),
        ),
    ]