# Generated by Django 4.2.1 on 2023-07-08 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0030_remove_mecanico_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mecanico',
            name='id_mecanico',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
