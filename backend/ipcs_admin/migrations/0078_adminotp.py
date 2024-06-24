# Generated by Django 5.0.1 on 2024-02-21 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipcs_admin', '0077_remove_servicereadytodispatch_item_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminOtp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('created_time', models.DateTimeField(auto_now=True)),
                ('otp', models.PositiveIntegerField()),
            ],
        ),
    ]