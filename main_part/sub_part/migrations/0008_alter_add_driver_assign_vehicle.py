# Generated by Django 3.2.3 on 2021-06-15 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0007_rename_permissiom_add_user_permission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_driver',
            name='assign_vehicle',
            field=models.CharField(max_length=50),
        ),
    ]