# Generated by Django 4.2.1 on 2023-07-08 00:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appweb', '0026_rename_id_atencion_mecanico_id_mecanico_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mecanico',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]