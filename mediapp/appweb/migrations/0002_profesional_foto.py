# Generated by Django 4.2.1 on 2023-05-26 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profesional',
            name='foto',
            field=models.ImageField(null=True, upload_to='profesionales'),
        ),
    ]
