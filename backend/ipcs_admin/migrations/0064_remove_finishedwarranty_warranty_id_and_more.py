# Generated by Django 5.0.1 on 2024-02-17 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipcs_admin', '0063_finishedwarranty'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='finishedwarranty',
            name='warranty_id',
        ),
        migrations.AlterField(
            model_name='finishedwarranty',
            name='id',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
