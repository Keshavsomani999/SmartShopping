# Generated by Django 4.0.4 on 2022-12-29 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_product_image2_product_image3_product_image4'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, default='', max_length=20000, null=True),
        ),
    ]
