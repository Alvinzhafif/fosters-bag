# Generated by Django 4.2.5 on 2023-11-17 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_product_rarity'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_discount',
            field=models.BooleanField(default=False),
        ),
    ]
