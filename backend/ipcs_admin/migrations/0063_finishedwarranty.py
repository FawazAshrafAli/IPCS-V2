# Generated by Django 5.0.1 on 2024-02-17 10:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipcs_admin', '0062_rename_application_date_approvedwarrantyapplication_application_datetime_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FinishedWarranty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('warranty_id', models.CharField(max_length=50)),
                ('approved_datetime', models.DateTimeField()),
                ('application_datetime', models.DateTimeField()),
                ('finished_datetime', models.DateTimeField()),
                ('customer_name', models.CharField(max_length=150)),
                ('contact_number', models.CharField(max_length=20)),
                ('email_id', models.EmailField(max_length=254)),
                ('alternative_number', models.CharField(blank=True, max_length=20, null=True)),
                ('billing_name', models.CharField(max_length=150)),
                ('invoice_number', models.CharField(max_length=50)),
                ('serial_number', models.CharField(max_length=50)),
                ('model_number', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('product_complain', models.TextField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ipcs_admin.product')),
            ],
        ),
    ]
