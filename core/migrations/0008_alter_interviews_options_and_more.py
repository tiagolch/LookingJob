# Generated by Django 4.1.1 on 2022-12-15 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_appliedcompanies_interviews_processes_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='interviews',
            options={'verbose_name': 'interview', 'verbose_name_plural': 'interviews'},
        ),
        migrations.RemoveField(
            model_name='appliedcompanies',
            name='process',
        ),
        migrations.AddField(
            model_name='processes',
            name='applied_company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.appliedcompanies'),
            preserve_default=False,
        ),
    ]
