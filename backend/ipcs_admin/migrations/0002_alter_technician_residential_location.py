# Generated by Django 5.0 on 2024-01-15 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipcs_admin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technician',
            name='residential_location',
            field=models.TextField(),
        ),
    ]