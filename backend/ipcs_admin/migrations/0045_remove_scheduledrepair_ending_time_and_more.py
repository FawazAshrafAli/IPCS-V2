# Generated by Django 5.0.1 on 2024-02-14 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipcs_admin', '0044_alter_approvedwarrantyapplication_feedback'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scheduledrepair',
            name='ending_time',
        ),
        migrations.RemoveField(
            model_name='scheduledrepair',
            name='repair_date',
        ),
        migrations.RemoveField(
            model_name='scheduledrepair',
            name='repair_request',
        ),
        migrations.RemoveField(
            model_name='scheduledrepair',
            name='starting_time',
        ),
        migrations.RemoveField(
            model_name='scheduledrepair',
            name='technician',
        ),
        migrations.AddField(
            model_name='scheduledrepair',
            name='address_customer',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scheduledrepair',
            name='alternative_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='scheduledrepair',
            name='contact_number',
            field=models.CharField(default=None, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scheduledrepair',
            name='customer_name',
            field=models.CharField(default=None, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scheduledrepair',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True, default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scheduledrepair',
            name='email_id',
            field=models.EmailField(default=None, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scheduledrepair',
            name='item_description',
            field=models.CharField(default=None, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scheduledrepair',
            name='model_number',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scheduledrepair',
            name='product',
            field=models.CharField(default=None, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scheduledrepair',
            name='serial_number',
            field=models.CharField(default=None, max_length=50, unique=True),
            preserve_default=False,
        ),
    ]
