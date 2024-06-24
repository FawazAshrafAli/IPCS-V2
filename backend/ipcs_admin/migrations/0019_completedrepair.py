# Generated by Django 5.0 on 2024-01-17 07:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipcs_admin', '0018_alter_completedservice_id_alter_repairrequest_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompletedRepair',
            fields=[
                ('id', models.CharField(editable=False, max_length=50, primary_key=True, serialize=False)),
                ('customer_name', models.CharField(max_length=150)),
                ('address_customer', models.TextField()),
                ('email_id', models.EmailField(max_length=254)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('item_name', models.CharField(max_length=150)),
                ('contact_number', models.CharField(max_length=20)),
                ('alternative_number', models.CharField(blank=True, max_length=20, null=True)),
                ('serial_number', models.CharField(max_length=50, unique=True)),
                ('item_description', models.CharField(max_length=200)),
                ('error_raised', models.CharField(max_length=250)),
                ('repair_date', models.DateField()),
                ('starting_time', models.TimeField()),
                ('ending_time', models.TimeField()),
                ('technician', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ipcs_admin.technician')),
            ],
        ),
    ]