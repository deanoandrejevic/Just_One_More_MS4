# Generated by Django 3.2 on 2022-01-06 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_platform'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='age_rating',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
    ]
