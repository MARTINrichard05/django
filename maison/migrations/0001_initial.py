# Generated by Django 5.0.4 on 2024-06-19 13:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='capteur',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('nomCapteur', models.CharField(max_length=100)),
                ('Emplacement', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='donnee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.IntegerField()),
                ('timestamp', models.DateTimeField()),
                ('id_capteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maison.capteur')),
            ],
        ),
    ]
