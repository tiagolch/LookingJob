# Generated by Django 4.1.1 on 2022-11-25 10:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_companies_active_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companies',
            name='submition_date',
            field=models.DateField(blank=True, default=datetime.date(2022, 11, 25), verbose_name='Data de inscrição'),
        ),
    ]
