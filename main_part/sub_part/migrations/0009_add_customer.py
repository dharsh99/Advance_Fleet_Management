# Generated by Django 3.2.3 on 2021-06-15 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0008_alter_add_driver_assign_vehicle'),
    ]

    operations = [
        migrations.CreateModel(
            name='Add_Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=100)),
                ('email_id', models.CharField(max_length=100)),
                ('radio', models.CharField(max_length=100)),
                ('address_details', models.CharField(max_length=100)),
            ],
        ),
    ]