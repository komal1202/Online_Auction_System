# Generated by Django 5.0.6 on 2024-08-13 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auction_app', '0011_images_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]