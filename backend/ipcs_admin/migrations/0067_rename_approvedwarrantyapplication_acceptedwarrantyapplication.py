# Generated by Django 5.0.1 on 2024-02-17 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ipcs_admin', '0066_alter_finishedwarranty_finished_datetime'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ApprovedWarrantyApplication',
            new_name='AcceptedWarrantyApplication',
        ),
    ]
