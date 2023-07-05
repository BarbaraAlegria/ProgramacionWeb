# Generated by Django 4.2.1 on 2023-07-03 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0015_atencion_motivorechazo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='atencion',
            name='id',
        ),
        migrations.AddField(
            model_name='atencion',
            name='id_Atencion',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='atencion',
            name='motivoRechazo',
            field=models.TextField(blank=True, null=True),
        ),
    ]
