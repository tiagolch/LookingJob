# Generated by Django 3.2.16 on 2022-12-19 19:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_appliedcompanies_submition_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appliedcompanies',
            name='submition_date',
            field=models.DateField(blank=True, default=datetime.date(2022, 12, 19), verbose_name='Data de inscrição'),
        ),
    ]
