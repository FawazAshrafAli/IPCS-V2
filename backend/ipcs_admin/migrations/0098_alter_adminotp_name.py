# Generated by Django 5.0.1 on 2024-04-18 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipcs_admin', '0097_alter_adminotp_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminotp',
            name='name',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
