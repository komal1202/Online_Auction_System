# Generated by Django 5.0.6 on 2024-08-27 04:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auction_app', '0012_product_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin_Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('admin', models.ForeignKey(limit_choices_to={'user_type': 1}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Seller_Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('seller_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Auction_app.seller')),
            ],
        ),
    ]