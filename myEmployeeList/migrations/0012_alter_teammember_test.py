# Generated by Django 4.2.7 on 2023-12-08 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myEmployeeList', '0011_teammember_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammember',
            name='test',
            field=models.BooleanField(choices=[('student', 'Student'), ('teacher', 'Teacher')], default='student', max_length=10),
        ),
    ]
