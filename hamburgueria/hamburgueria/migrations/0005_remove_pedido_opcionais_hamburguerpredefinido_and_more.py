# Generated by Django 5.0.6 on 2024-06-05 19:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hamburgueria', '0004_opcionais_alter_pedido_opcionais'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='opcionais',
        ),
        migrations.CreateModel(
            name='HamburguerPredefinido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('carne', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hamburgueria.carne')),
                ('opcionais', models.ManyToManyField(to='hamburgueria.opcionais')),
                ('pao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hamburgueria.pao')),
            ],
        ),
        migrations.AddField(
            model_name='pedido',
            name='opcionais',
            field=models.ManyToManyField(to='hamburgueria.opcionais'),
        ),
    ]
