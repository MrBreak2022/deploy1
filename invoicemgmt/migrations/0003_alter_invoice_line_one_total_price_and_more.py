# Generated by Django 4.1.1 on 2022-11-08 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoicemgmt', '0002_alter_invoice_invoice_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='line_one_total_price',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Total (PHP):'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='line_three_total_price',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Total (PHP):'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='line_two_total_price',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Total (PHP):'),
        ),
    ]
