# Generated by Django 2.2.5 on 2019-10-07 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('creditdata', '0023_auto_20191004_1340'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='testingdata',
            options={'verbose_name': 'Index Price', 'verbose_name_plural': 'Index Price'},
        ),
        migrations.AlterModelTable(
            name='testingdata',
            table='Index Price',
        ),
    ]
