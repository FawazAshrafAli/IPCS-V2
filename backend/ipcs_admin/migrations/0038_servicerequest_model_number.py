# Generated by Django 5.0.1 on 2024-02-08 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipcs_admin', '0037_remove_approvedwarrantyapplication_duration_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicerequest',
            name='model_number',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
    ]