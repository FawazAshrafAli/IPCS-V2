# Generated by Django 5.0.1 on 2024-04-30 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipcs_admin', '0099_rename_name_adminotp_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rejectedwarranty',
            name='reason',
            field=models.TextField(blank=True, null=True),
        ),
    ]