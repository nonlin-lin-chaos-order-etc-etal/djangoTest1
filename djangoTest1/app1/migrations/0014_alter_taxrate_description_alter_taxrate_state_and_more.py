# Generated by Django 4.1.1 on 2022-09-10 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0013_alter_taxrate_description_alter_taxrate_tax_rate_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taxrate',
            name='description',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='taxrate',
            name='state',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='taxrate',
            name='tax_rate_id',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
    ]
