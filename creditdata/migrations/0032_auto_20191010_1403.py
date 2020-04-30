# Generated by Django 2.2.5 on 2019-10-10 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creditdata', '0031_return'),
    ]

    operations = [
        migrations.AlterField(
            model_name='return',
            name='decimalpoint_500',
            field=models.DecimalField(db_column='decimalpoint_500', decimal_places=5, default=None, help_text='Amount of returns achieved by Decimal point 500 index', max_digits=5, verbose_name='Decimal Point 500'),
        ),
        migrations.AlterField(
            model_name='return',
            name='sn500',
            field=models.DecimalField(db_column='sn500', decimal_places=5, default=None, help_text='Amount of returns achieved by SN 500 index', max_digits=5, verbose_name='SN 500'),
        ),
    ]