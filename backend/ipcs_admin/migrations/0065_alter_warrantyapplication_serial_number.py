# Generated by Django 5.0.1 on 2024-02-17 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipcs_admin', '0064_remove_finishedwarranty_warranty_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warrantyapplication',
            name='serial_number',
            field=models.CharField(max_length=50),
        ),
    ]
