# Generated by Django 4.2.7 on 2023-12-08 03:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myEmployeeList', '0014_remove_teammember_test_teammember_is_student_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teammember',
            name='role',
        ),
    ]
