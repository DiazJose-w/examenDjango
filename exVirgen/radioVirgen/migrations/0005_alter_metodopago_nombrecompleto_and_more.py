# Generated by Django 5.1.4 on 2025-02-21 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('radioVirgen', '0004_metodopago'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metodopago',
            name='nombreCompleto',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='metodopago',
            name='numeroCuenta',
            field=models.IntegerField(unique=True),
        ),
    ]
