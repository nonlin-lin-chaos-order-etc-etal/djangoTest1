# Generated by Django 4.1.1 on 2022-09-10 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0011_taxrate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taxrate',
            name='created',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='taxrate',
            name='state',
            field=models.CharField(default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='taxrate',
            name='tax_rate_id',
            field=models.CharField(default='', max_length=255, null=True),
        ),
    ]