# Generated by Django 4.1.1 on 2022-12-16 02:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_appliedcompanies_process_processes_owner_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='processes',
            name='applied_company',
        ),
    ]
