# Generated by Django 3.2.15 on 2022-12-19 02:50

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TransportationRequest',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('source', models.CharField(max_length=500, verbose_name='Asset to be Picked From')),
                ('destination', models.CharField(max_length=500, verbose_name='Asset Delivered to')),
                ('pick_on', models.DateTimeField(verbose_name='Asset to be picked up on')),
                ('no_of_assets', models.PositiveIntegerField()),
                ('asset_type', models.CharField(choices=[('laptop', 'laptop'), ('package', 'package'), ('travel_bag', 'travel_bag')], max_length=30)),
                ('asset_sensitivity', models.CharField(choices=[('highly_sensitive', 'highly_sensitive'), ('sensitive', 'sensitive'), ('high', 'high')], max_length=30)),
                ('status', models.CharField(choices=[('confirm', 'confirm'), ('pending', 'pending'), ('expired', 'expired')], max_length=50)),
                ('whom_to_deliver', models.CharField(max_length=300)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
