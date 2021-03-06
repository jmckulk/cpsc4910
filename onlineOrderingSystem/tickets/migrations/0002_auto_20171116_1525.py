# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-16 20:25
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_auto_20171116_1525'),
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Addition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='menu.Topping')),
            ],
        ),
        migrations.CreateModel(
            name='Subtraction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RenameModel(
            old_name='order',
            new_name='Meal',
        ),
        migrations.RemoveField(
            model_name='side',
            name='order',
        ),
        migrations.AddField(
            model_name='side',
            name='ticket',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tickets.Ticket'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ticket',
            name='fulfilled',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='meal',
            name='drink',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='menu.Drink'),
        ),
        migrations.AlterField(
            model_name='meal',
            name='meal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='menu.Meal'),
        ),
        migrations.AlterField(
            model_name='meal',
            name='ticket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.Ticket'),
        ),
        migrations.AlterField(
            model_name='side',
            name='side',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='menu.Side'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='customer_phone_number',
            field=models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='price_posttax_total',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='price_pretax_total',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='price_tax',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='subtraction',
            name='meal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tickets.Meal'),
        ),
        migrations.AddField(
            model_name='subtraction',
            name='side',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tickets.Side'),
        ),
        migrations.AddField(
            model_name='subtraction',
            name='sub',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='menu.Topping'),
        ),
        migrations.AddField(
            model_name='addition',
            name='meal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tickets.Meal'),
        ),
        migrations.AddField(
            model_name='addition',
            name='side',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tickets.Side'),
        ),
    ]
