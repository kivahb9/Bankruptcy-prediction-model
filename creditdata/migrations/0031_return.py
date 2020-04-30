# Generated by Django 2.2.5 on 2019-10-10 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creditdata', '0030_delete_return'),
    ]

    operations = [
        migrations.CreateModel(
            name='Return',
            fields=[
                ('id', models.AutoField(db_column='id', help_text='Auto incremental unique interger values.', primary_key=True, serialize=False, verbose_name='Id')),
                ('return_appreciation', models.CharField(db_column='return_appreciation', default=None, help_text='Time span', max_length=50, verbose_name='Return Appreciation')),
                ('date', models.DateField(auto_now_add=True, db_column='date', null=True, verbose_name='Date')),
                ('sn500', models.DecimalField(db_column='sn500', decimal_places=2, default=None, help_text='Amount of returns achieved by SN 500 index', max_digits=4, verbose_name='SN 500')),
                ('decimalpoint_500', models.DecimalField(db_column='decimalpoint_500', decimal_places=2, default=None, help_text='Amount of returns achieved by Decimal point 500 index', max_digits=4, verbose_name='Decimal Point 500')),
            ],
            options={
                'verbose_name': 'Returns',
                'verbose_name_plural': 'Returns',
                'db_table': 'Returns',
            },
        ),
    ]