# Generated by Django 3.2.3 on 2021-06-23 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0026_remove_reg_manage_vehicle_assigned_driver'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reg_manage_vehicle',
            name='registration_expiry',
            field=models.DateField(),
        ),
    ]
