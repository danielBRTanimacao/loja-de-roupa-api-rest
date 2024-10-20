# Generated by Django 5.1.2 on 2024-10-18 18:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('origin', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Clothing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('value', models.DecimalField(decimal_places=2, max_digits=3)),
                ('size', models.CharField(choices=[('PP', 'PP'), ('P', 'P'), ('M', 'M'), ('G', 'G'), ('GG', 'GG'), ('XG', 'XG')], max_length=2)),
                ('color', models.CharField(max_length=50)),
                ('stock', models.PositiveIntegerField(default=0)),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('mark', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.mark')),
            ],
            options={
                'verbose_name': 'Clothing',
                'verbose_name_plural': 'Clothes',
            },
        ),
    ]
