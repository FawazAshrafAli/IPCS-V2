# Generated by Django 5.0.1 on 2024-02-22 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0012_alter_customer_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='photo',
            field=models.ImageField(upload_to='customer_pics/'),
        ),
    ]
