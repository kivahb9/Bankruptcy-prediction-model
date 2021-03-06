# Generated by Django 2.2.4 on 2019-08-30 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creditdata', '0002_auto_20190830_1307'),
    ]

    operations = [
        migrations.AddField(
            model_name='constituentmaster',
            name='bb_ticker',
            field=models.CharField(db_column='BB_ticker', default=0, help_text='Unique identifier', max_length=50, verbose_name='BB ticker'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='constituentmaster',
            name='currency',
            field=models.DecimalField(db_column='CURRENCY', decimal_places=10, default=0, help_text='Type of currency', max_digits=60, verbose_name='Currency'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='constituentmaster',
            name='region',
            field=models.CharField(db_column='REGION', default=0, help_text='Country', max_length=50, verbose_name='Region'),
            preserve_default=False,
        ),
    ]
