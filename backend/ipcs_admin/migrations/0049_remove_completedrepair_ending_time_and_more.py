# Generated by Django 5.0.1 on 2024-02-14 06:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ipcs_admin', '0048_rename_startedrepairs_startedrepair'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='completedrepair',
            name='ending_time',
        ),
        migrations.RemoveField(
            model_name='completedrepair',
            name='repair_date',
        ),
        migrations.RemoveField(
            model_name='completedrepair',
            name='starting_time',
        ),
        migrations.RemoveField(
            model_name='completedrepair',
            name='technician',
        ),
    ]