# Generated by Django 2.2.4 on 2019-08-30 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creditdata', '0005_auto_20190830_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='constituentmaster',
            name='bb_ticker',
            field=models.CharField(db_column='bb_ticker', help_text='Unique identifier', max_length=50, null=True, verbose_name='BB ticker'),
        ),
        migrations.AlterField(
            model_name='constituentmaster',
            name='company_name',
            field=models.CharField(db_column='company_name', help_text='Name of the company holding shares', max_length=50, null=True, verbose_name='Company Name'),
        ),
        migrations.AlterField(
            model_name='constituentmaster',
            name='currency',
            field=models.CharField(db_column='currency', help_text='Type of currency', max_length=50, null=True, verbose_name='Currency'),
        ),
        migrations.AlterField(
            model_name='constituentmaster',
            name='gics_sector_code',
            field=models.IntegerField(db_column='gics_sector_code', help_text='Differentiates each sector according to its code', null=True, verbose_name='GICS SECTOR CODE'),
        ),
        migrations.AlterField(
            model_name='constituentmaster',
            name='gics_sector_name',
            field=models.CharField(db_column='gics_sector_name', help_text='Name of the sector', max_length=50, null=True, verbose_name='GICS SECTOR NAME'),
        ),
        migrations.AlterField(
            model_name='constituentmaster',
            name='region',
            field=models.CharField(db_column='region', help_text='Country', max_length=50, null=True, verbose_name='Region'),
        ),
    ]
