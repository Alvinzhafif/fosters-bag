# Generated by Django 4.2.5 on 2023-09-16 01:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_product_amount_product_armor_product_bow_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='armor',
            new_name='type',
        ),
        migrations.RemoveField(
            model_name='product',
            name='bow',
        ),
    ]
