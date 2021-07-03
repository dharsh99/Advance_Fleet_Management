# Generated by Django 3.2.3 on 2021-06-29 04:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0033_reg_vehicle_group_is_enable'),
    ]

    operations = [
        migrations.AddField(
            model_name='manage_income',
            name='plate',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='manage_income',
            name='vehicle_model',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='manage_income',
            name='income_amount',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='manage_income',
            name='milege',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='manage_income',
            name='total_amount',
            field=models.IntegerField(max_length=100),
        ),
        migrations.AlterField(
            model_name='manage_income',
            name='total_tax',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='manage_income',
            name='total_tax_charge',
            field=models.CharField(max_length=100),
        ),
    ]
