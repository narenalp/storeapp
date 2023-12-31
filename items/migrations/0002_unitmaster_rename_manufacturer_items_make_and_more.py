# Generated by Django 5.0 on 2023-12-17 04:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UnitMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.CharField(max_length=6)),
            ],
        ),
        migrations.RenameField(
            model_name='items',
            old_name='Manufacturer',
            new_name='Make',
        ),
        migrations.AddField(
            model_name='items',
            name='category',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='items',
            name='date_added',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='items',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='items',
            name='unit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='items.unitmaster'),
        ),
    ]
