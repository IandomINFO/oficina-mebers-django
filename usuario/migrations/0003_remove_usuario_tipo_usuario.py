# Generated by Django 4.2.5 on 2023-11-14 16:36

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("usuario", "0002_usuario_tipo_usuario"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="usuario",
            name="tipo_usuario",
        ),
    ]