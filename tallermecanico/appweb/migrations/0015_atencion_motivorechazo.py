# Generated by Django 4.2.1 on 2023-06-30 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0014_alter_atencion_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='atencion',
            name='motivoRechazo',
            field=models.TextField(null=True),
        ),
    ]
