# Generated by Django 5.0.1 on 2024-02-22 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipcs_admin', '0079_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='link',
            field=models.URLField(blank=True, max_length=250, null=True),
        ),
    ]