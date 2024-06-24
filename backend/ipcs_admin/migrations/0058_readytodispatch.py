# Generated by Django 5.0.1 on 2024-02-16 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipcs_admin', '0057_rename_address_customer_startedservice_address_site'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReadyToDispatch',
            fields=[
                ('id', models.CharField(editable=False, max_length=50, primary_key=True, serialize=False)),
                ('application_datetime', models.DateTimeField()),
                ('started_datetime', models.DateTimeField()),
                ('completion_datetime', models.DateTimeField()),
                ('dispatch_ready_datetime', models.DateTimeField(auto_now_add=True)),
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
    ]