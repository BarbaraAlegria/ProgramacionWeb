# Generated by Django 4.2.1 on 2023-07-08 01:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0029_alter_mecanico_options_remove_mecanico_date_joined_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mecanico',
            name='usuario',
        ),
    ]
