# Generated by Django 4.2.1 on 2023-06-28 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0008_alter_mecanico_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atencion',
            name='fotografia',
            field=models.ImageField(null=True, upload_to='atenciones'),
        ),
    ]
