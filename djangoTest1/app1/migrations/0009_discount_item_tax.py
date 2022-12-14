# Generated by Django 4.1.1 on 2022-09-10 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_delete_discount_remove_item_order_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('price', models.IntegerField(default=0)),
                ('currency', models.CharField(default='usd', max_length=15)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.order')),
            ],
        ),
        migrations.CreateModel(
            name='Tax',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tax_behavior_inclusive', models.BooleanField(default=True)),
                ('tax_code', models.CharField(default='', max_length=255)),
                ('item', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='tax', to='app1.item')),
            ],
        ),
    ]
