# Generated by Django 5.0.1 on 2024-02-14 06:48

import ipcs_admin.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipcs_admin', '0050_delete_completedrepair_delete_repairrequest_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompletedRepair',
            fields=[
                ('id', models.CharField(editable=False, max_length=50, primary_key=True, serialize=False)),
                ('application_datetime', models.DateTimeField()),
                ('started_datetime', models.DateTimeField()),
                ('completion_datetime', models.DateTimeField(auto_now_add=True)),
                ('customer_name', models.CharField(max_length=150)),
                ('address_customer', models.TextField()),
                ('email_id', models.EmailField(max_length=254)),
                ('product', models.CharField(max_length=150)),
                ('contact_number', models.CharField(max_length=20)),
                ('alternative_number', models.CharField(blank=True, max_length=20, null=True)),
                ('serial_number', models.CharField(max_length=50)),
                ('model_number', models.CharField(max_length=50)),
                ('item_description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='RepairRequest',
            fields=[
                ('id', models.CharField(default=ipcs_admin.models.repair_unique_id, editable=False, max_length=50, primary_key=True, serialize=False)),
                ('customer_name', models.CharField(max_length=150)),
                ('address_customer', models.TextField()),
                ('email_id', models.EmailField(max_length=254)),
                ('application_datetime', models.DateTimeField(auto_now_add=True)),
                ('product', models.CharField(max_length=150)),
                ('contact_number', models.CharField(max_length=20)),
                ('alternative_number', models.CharField(blank=True, max_length=20, null=True)),
                ('serial_number', models.CharField(max_length=50, unique=True)),
                ('model_number', models.CharField(max_length=50)),
                ('item_description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='StartedRepair',
            fields=[
                ('id', models.CharField(editable=False, max_length=50, primary_key=True, serialize=False)),
                ('application_datetime', models.DateTimeField()),
                ('started_datetime', models.DateTimeField(auto_now_add=True)),
                ('customer_name', models.CharField(max_length=150)),
                ('address_customer', models.TextField()),
                ('email_id', models.EmailField(max_length=254)),
                ('product', models.CharField(max_length=150)),
                ('contact_number', models.CharField(max_length=20)),
                ('alternative_number', models.CharField(blank=True, max_length=20, null=True)),
                ('serial_number', models.CharField(max_length=50, unique=True)),
                ('model_number', models.CharField(max_length=50)),
                ('item_description', models.CharField(max_length=200)),
            ],
        ),
    ]
