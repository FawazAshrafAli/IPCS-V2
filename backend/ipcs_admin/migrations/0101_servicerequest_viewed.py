# Generated by Django 5.0.1 on 2024-04-30 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipcs_admin', '0100_alter_rejectedwarranty_reason'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicerequest',
            name='viewed',
            field=models.BooleanField(default=False),
        ),
    ]
