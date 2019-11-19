# Generated by Django 2.2.6 on 2019-11-19 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='auction_type',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='auction',
            name='description',
            field=models.TextField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='auction',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='end_time'),
        ),
        migrations.AlterField(
            model_name='auction',
            name='name',
            field=models.CharField(blank=True, default='An Auction', max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='auction',
            name='start_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='start_time'),
        ),
        migrations.AlterField(
            model_name='items',
            name='description',
            field=models.TextField(blank=True, default='item description', max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='items',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='item_image'),
        ),
        migrations.AlterField(
            model_name='items',
            name='name',
            field=models.CharField(default='An Item', max_length=256),
        ),
        migrations.AlterField(
            model_name='items',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, default='00.00', max_digits=6, null=True),
        ),
    ]
