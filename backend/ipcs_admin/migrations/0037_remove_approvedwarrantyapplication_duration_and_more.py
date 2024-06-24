# Generated by Django 5.0.1 on 2024-02-05 09:42

import ipcs_admin.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipcs_admin', '0036_alter_client_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='approvedwarrantyapplication',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='approvedwarrantyapplication',
            name='expiry_date',
        ),
        migrations.RemoveField(
            model_name='approvedwarrantyapplication',
            name='purchase_date',
        ),
        migrations.RemoveField(
            model_name='claimedwarranty',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='claimedwarranty',
            name='expiry_date',
        ),
        migrations.RemoveField(
            model_name='claimedwarranty',
            name='purchase_date',
        ),
        migrations.RemoveField(
            model_name='warrantyapplication',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='warrantyapplication',
            name='expiry_date',
        ),
        migrations.RemoveField(
            model_name='warrantyapplication',
            name='purchase_date',
        ),
        migrations.AlterField(
            model_name='warrantyapplication',
            name='id',
            field=models.CharField(default=ipcs_admin.models.warranty_unique_id, editable=False, max_length=50, primary_key=True, serialize=False),
        ),
        migrations.DeleteModel(
            name='Warranty',
        ),
    ]