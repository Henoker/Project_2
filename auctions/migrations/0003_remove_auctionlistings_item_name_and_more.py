# Generated by Django 4.0.1 on 2022-04-29 13:33

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_alter_auctionlistings_watchlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auctionlistings',
            name='item_name',
        ),
        migrations.AddField(
            model_name='auctionlistings',
            name='name_of_item',
            field=models.CharField(default='exit', max_length=32),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='auctionlistings',
            name='description',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='auctionlistings',
            name='watchlist',
            field=models.ManyToManyField(blank=True, related_name='watch_listings', to=settings.AUTH_USER_MODEL),
        ),
    ]
