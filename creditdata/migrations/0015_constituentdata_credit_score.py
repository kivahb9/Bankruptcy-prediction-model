# Generated by Django 2.2.4 on 2019-09-26 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creditdata', '0014_auto_20190924_1833'),
    ]

    operations = [
        migrations.AddField(
            model_name='constituentdata',
            name='credit_score',
            field=models.DecimalField(db_column='credit_score', decimal_places=10, default=2, max_digits=15, verbose_name='Credit Score'),
            preserve_default=False,
        ),
    ]
