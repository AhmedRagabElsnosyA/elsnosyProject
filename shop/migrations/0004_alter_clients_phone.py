# Generated by Django 4.2 on 2023-12-25 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_clients_addition_alter_clients_left_cyl_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='phone',
            field=models.CharField(blank=True, max_length=11),
        ),
    ]
