# Generated by Django 4.2.7 on 2023-12-07 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myEmployeeList', '0002_alter_teammember_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammember',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
