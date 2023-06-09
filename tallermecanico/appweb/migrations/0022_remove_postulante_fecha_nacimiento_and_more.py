# Generated by Django 4.2.1 on 2023-07-04 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0021_alter_atencion_id_atencion_postulante'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postulante',
            name='fecha_nacimiento',
        ),
        migrations.RemoveField(
            model_name='postulante',
            name='rut',
        ),
        migrations.AddField(
            model_name='postulante',
            name='email',
            field=models.EmailField(default='', max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='postulante',
            name='id_postulante',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
    ]
