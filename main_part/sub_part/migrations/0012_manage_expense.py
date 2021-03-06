# Generated by Django 3.2.3 on 2021-06-16 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0011_manage_income'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manage_Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('select_vehicle', models.CharField(max_length=100)),
                ('expense_type', models.CharField(max_length=100)),
                ('select_vendor', models.CharField(max_length=100)),
                ('total_amount', models.IntegerField()),
                ('note', models.CharField(max_length=100)),
                ('date', models.DateField()),
            ],
        ),
    ]
