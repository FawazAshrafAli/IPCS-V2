# Generated by Django 5.0.1 on 2024-03-01 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipcs_admin', '0089_completedservice_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='repairreadytodispatch',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='repair_ready_to_dispatch_files/'),
        ),
    ]
