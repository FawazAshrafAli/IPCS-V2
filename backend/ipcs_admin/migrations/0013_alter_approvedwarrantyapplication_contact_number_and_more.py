# Generated by Django 5.0 on 2024-01-16 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipcs_admin', '0012_completedservice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='approvedwarrantyapplication',
            name='contact_number',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='approvedwarrantyapplication',
            name='email_id',
            field=models.EmailField(max_length=254),
        ),
    ]