# Generated by Django 5.0.1 on 2024-02-20 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipcs_admin', '0074_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='images/default_images/other_products.jpeg', upload_to='product_images/'),
        ),
    ]
