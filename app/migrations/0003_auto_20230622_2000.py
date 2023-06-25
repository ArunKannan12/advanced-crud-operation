# Generated by Django 3.2.19 on 2023-06-22 14:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20230622_0954'),
    ]

    operations = [
        migrations.CreateModel(
            name='position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_position', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='emp_details',
            name='emp_id',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^[1-9]{1}[0-9]{2}\\s{0,1}[0-9]{3}$', 'Enter a valid employee id')]),
        ),
    ]
