# Generated by Django 4.0.6 on 2022-08-25 19:08

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.IntegerField(default=0)),
                ('account_type', models.CharField(max_length=20, null=True)),
                ('balance', models.IntegerField()),
                ('name', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('country_of_origin', models.CharField(max_length=24, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20, null=True)),
                ('last_name', models.CharField(max_length=20, null=True)),
                ('age', models.CharField(max_length=20, null=True)),
                ('address', models.CharField(max_length=20, null=True)),
                ('phonenumber', models.CharField(max_length=15, null=True)),
                ('email', models.EmailField(max_length=25, null=True)),
                ('nationality', models.CharField(max_length=20, null=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('profile_picture', models.ImageField(null=True, upload_to='profile_pictures/')),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(max_length=20, null=True)),
                ('pin', models.TextField(max_length=6, null=True)),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Wallet_currency', to='wallet.currency')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Wallet_customer', to='wallet.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_reference', models.CharField(max_length=200, null=True)),
                ('transaction_amount', models.IntegerField()),
                ('transaction_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('actual_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Transaction_account', to='wallet.account')),
                ('last_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Transaction_last_account', to='wallet.account')),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Transaction_wallet', to='wallet.wallet')),
            ],
        ),
        migrations.CreateModel(
            name='ThirdParty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, null=True)),
                ('phonenumber', models.IntegerField()),
                ('thirdparty_id', models.CharField(max_length=20, null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ThirdParty_account', to='wallet.account')),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ThirdParty_currency', to='wallet.currency')),
            ],
        ),
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True)),
                ('bonus', models.CharField(max_length=25, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Reward_customer', to='wallet.customer')),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Reward_transaction', to='wallet.transaction')),
            ],
        ),
        migrations.CreateModel(
            name='Receipts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receipt_type', models.CharField(max_length=25, null=True)),
                ('receipt_number', models.CharField(max_length=25, null=True)),
                ('receipt_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('totalAmount', models.IntegerField(default=0)),
                ('receiptFile', models.FileField(upload_to='wallet/')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Receipt_account', to='wallet.account')),
            ],
        ),
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification_id', models.CharField(max_length=25, null=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('receipts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Notifications_receipts', to='wallet.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_number', models.IntegerField()),
                ('loan_type', models.CharField(max_length=25, null=True)),
                ('amount', models.IntegerField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('interest_rate', models.IntegerField()),
                ('due_date', models.DateField(default=django.utils.timezone.now)),
                ('loan_balance', models.IntegerField()),
                ('loan_term', models.IntegerField()),
                ('guaranter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Loan_guaranter', to='wallet.customer')),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Loan_wallet', to='wallet.wallet')),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_name', models.CharField(max_length=20, null=True)),
                ('card_number', models.IntegerField()),
                ('security_code', models.IntegerField()),
                ('issue_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('expiry_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Card_account', to='wallet.account')),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Card_Wallet', to='wallet.wallet')),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='wallet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Account_wallet', to='wallet.wallet'),
        ),
    ]
