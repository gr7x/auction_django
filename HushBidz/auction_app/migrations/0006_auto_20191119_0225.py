# Generated by Django 2.2.6 on 2019-11-19 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction_app', '0005_auto_20191119_0222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='auction_type',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='auction_type'),
        ),
    ]
