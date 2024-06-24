# Generated by Django 5.0.1 on 2024-03-05 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ipcs_admin', '0091_repairreadytodispatch_remark'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rejectedwarranty',
            name='product',
        ),
        migrations.RemoveField(
            model_name='warrantyapplication',
            name='product',
        ),
        migrations.DeleteModel(
            name='FinishedWarranty',
        ),
        migrations.DeleteModel(
            name='RejectedWarranty',
        ),
        migrations.DeleteModel(
            name='WarrantyApplication',
        ),
    ]
