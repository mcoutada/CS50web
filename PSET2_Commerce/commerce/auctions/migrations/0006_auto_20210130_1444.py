# Generated by Django 2.2.12 on 2021-01-30 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_auto_20210127_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='auctions\\static\x07uctions\\img'),
        ),
    ]