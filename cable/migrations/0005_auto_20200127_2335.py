# Generated by Django 3.0.2 on 2020-01-27 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cable', '0004_auto_20200127_0100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='residencdimens',
            name='r_nominal_chain',
            field=models.FloatField(blank=True, verbose_name='Corrente Nominal'),
        ),
    ]
