# Generated by Django 5.0.1 on 2024-02-15 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipcs_admin', '0055_delete_completedservice'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompletedService',
            fields=[
                ('id', models.CharField(editable=False, max_length=50, primary_key=True, serialize=False)),
                ('started_datetime', models.DateTimeField()),
                ('completion_datetime', models.DateTimeField(auto_now_add=True)),
                ('customer_name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('application_datetime', models.DateTimeField(auto_now_add=True)),
                ('alternative_number', models.CharField(blank=True, max_length=20, null=True)),
                ('address_site', models.TextField()),
                ('product', models.CharField(max_length=150)),
                ('contact_number', models.CharField(max_length=20)),
                ('serial_number', models.CharField(max_length=50)),
                ('model_number', models.CharField(blank=True, max_length=50, null=True)),
                ('service_description', models.CharField(max_length=250)),
            ],
        ),
    ]