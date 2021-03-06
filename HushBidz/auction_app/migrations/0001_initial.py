# Generated by Django 2.2.6 on 2019-11-12 00:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('auction_type', models.BooleanField()),
                ('description', models.TextField(max_length=256)),
                ('start_time', models.DateTimeField(verbose_name='start_time')),
                ('end_time', models.DateTimeField(verbose_name='end_time')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('description', models.TextField(max_length=256)),
                ('image', models.ImageField(upload_to='item_image')),
                ('auction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='auction_app.Auction')),
            ],
        ),
    ]
