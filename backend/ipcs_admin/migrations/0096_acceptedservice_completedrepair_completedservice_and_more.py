# Generated by Django 5.0.1 on 2024-03-05 16:11

import django.db.models.deletion
import ipcs_admin.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipcs_admin', '0095_delete_acceptedservice_delete_completedrepair_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcceptedService',
            fields=[
                ('id', models.CharField(editable=False, max_length=50, primary_key=True, serialize=False)),
                ('application_datetime', models.DateTimeField()),
                ('accepted_datetime', models.DateTimeField(auto_now_add=True)),
                ('customer_name', models.CharField(max_length=150)),
                ('address_site', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('contact_number', models.CharField(max_length=20)),
                ('alternative_number', models.CharField(blank=True, max_length=20, null=True)),
                ('serial_number', models.CharField(max_length=50, unique=True)),
                ('model_number', models.CharField(blank=True, max_length=50, null=True)),
                ('service_description', models.TextField()),
                ('remark', models.TextField(blank=True, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ipcs_admin.product')),
            ],
        ),
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
                ('contact_number', models.CharField(max_length=20)),
                ('alternative_number', models.CharField(blank=True, max_length=20, null=True)),
                ('serial_number', models.CharField(max_length=50)),
                ('model_number', models.CharField(max_length=50)),
                ('item_description', models.TextField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ipcs_admin.product')),
            ],
        ),
        migrations.CreateModel(
            name='CompletedService',
            fields=[
                ('id', models.CharField(editable=False, max_length=50, primary_key=True, serialize=False)),
                ('application_datetime', models.DateTimeField()),
                ('accepted_datetime', models.DateTimeField()),
                ('completion_datetime', models.DateTimeField(auto_now_add=True)),
                ('customer_name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('alternative_number', models.CharField(blank=True, max_length=20, null=True)),
                ('address_site', models.TextField()),
                ('contact_number', models.CharField(max_length=20)),
                ('serial_number', models.CharField(max_length=50)),
                ('model_number', models.CharField(blank=True, max_length=50, null=True)),
                ('service_description', models.TextField()),
                ('remark', models.TextField(blank=True, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='completed service files/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ipcs_admin.product')),
            ],
        ),
        migrations.CreateModel(
            name='RepairReadyToDispatch',
            fields=[
                ('id', models.CharField(editable=False, max_length=50, primary_key=True, serialize=False)),
                ('application_datetime', models.DateTimeField()),
                ('started_datetime', models.DateTimeField()),
                ('completion_datetime', models.DateTimeField()),
                ('dispatch_ready_datetime', models.DateTimeField(auto_now_add=True)),
                ('customer_name', models.CharField(max_length=150)),
                ('address_customer', models.TextField()),
                ('email_id', models.EmailField(max_length=254)),
                ('contact_number', models.CharField(max_length=20)),
                ('alternative_number', models.CharField(blank=True, max_length=20, null=True)),
                ('serial_number', models.CharField(max_length=50)),
                ('model_number', models.CharField(max_length=50)),
                ('item_description', models.TextField()),
                ('remark', models.TextField(blank=True, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='repair_ready_to_dispatch_files/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ipcs_admin.product')),
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
                ('contact_number', models.CharField(max_length=20)),
                ('alternative_number', models.CharField(blank=True, max_length=20, null=True)),
                ('serial_number', models.CharField(max_length=50, unique=True)),
                ('model_number', models.CharField(max_length=50)),
                ('item_description', models.TextField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ipcs_admin.product')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceRequest',
            fields=[
                ('id', models.CharField(default=ipcs_admin.models.service_unique_id, editable=False, max_length=50, primary_key=True, serialize=False)),
                ('customer_name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('application_datetime', models.DateTimeField(auto_now_add=True)),
                ('alternative_number', models.CharField(blank=True, max_length=20, null=True)),
                ('address_site', models.TextField()),
                ('contact_number', models.CharField(max_length=20)),
                ('serial_number', models.CharField(max_length=50, unique=True)),
                ('model_number', models.CharField(blank=True, max_length=50, null=True)),
                ('service_description', models.TextField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ipcs_admin.product')),
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
                ('contact_number', models.CharField(max_length=20)),
                ('alternative_number', models.CharField(blank=True, max_length=20, null=True)),
                ('serial_number', models.CharField(max_length=50, unique=True)),
                ('model_number', models.CharField(max_length=50)),
                ('item_description', models.TextField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ipcs_admin.product')),
            ],
        ),
    ]
