# Generated by Django 4.2.5 on 2023-12-12 12:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("oficinamebers", "0013_produto_quantidade"),
    ]

    operations = [
        migrations.AlterField(
            model_name="itenscompra",
            name="quantidade",
            field=models.IntegerField(default=0),
        ),
    ]
