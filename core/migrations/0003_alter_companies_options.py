# Generated by Django 4.1.1 on 2022-10-13 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_companies_aplication_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='companies',
            options={'ordering': ['-updated_at'], 'verbose_name': 'Company', 'verbose_name_plural': 'Companies'},
        ),
    ]
