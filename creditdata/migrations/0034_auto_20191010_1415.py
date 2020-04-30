# Generated by Django 2.2.5 on 2019-10-10 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creditdata', '0033_auto_20191010_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='return',
            name='decimalpoint_500',
            field=models.CharField(db_column='decimalpoint_500', default=None, help_text='Amount of returns achieved by Decimal point 500 index', max_length=50, verbose_name='Decimal Point 500'),
        ),
        migrations.AlterField(
            model_name='return',
            name='sn500',
            field=models.CharField(db_column='sn500', default=None, help_text='Amount of returns achieved by SN 500 index', max_length=50, verbose_name='SN 500'),
        ),
    ]
