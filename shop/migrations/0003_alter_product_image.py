# Generated by Django 5.1.6 on 2025-02-27 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0002_product_created_at_product_updated_at_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.BinaryField(blank=True, editable=True, null=True),
        ),
    ]
