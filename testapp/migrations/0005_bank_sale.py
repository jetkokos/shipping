# Generated by Django 3.0.7 on 2020-06-29 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0004_broker_order_shipowner_vessel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=120)),
                ('address', models.CharField(max_length=120)),
                ('bank_name', models.CharField(max_length=120)),
                ('bank_address', models.CharField(max_length=120)),
                ('account_number', models.CharField(max_length=120)),
                ('swift_number', models.CharField(max_length=120)),
                ('routing_number', models.CharField(max_length=120)),
                ('wire_transfer_number', models.CharField(max_length=120)),
                ('currency', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('port', models.CharField(max_length=120)),
                ('country', models.CharField(max_length=120)),
                ('delivery_date', models.DateField()),
                ('delivery_moth', models.CharField(max_length=120)),
                ('payment_terms', models.CharField(max_length=120)),
            ],
        ),
    ]
