# Generated by Django 5.0.6 on 2024-08-06 01:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Auction_app', '0006_bidder_seller_delete_registrationmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seller',
            name='admin',
        ),
        migrations.DeleteModel(
            name='Bidder',
        ),
        migrations.DeleteModel(
            name='Seller',
        ),
    ]
