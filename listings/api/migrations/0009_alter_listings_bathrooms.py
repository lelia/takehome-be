# Generated by Django 3.2.16 on 2022-11-21 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20221121_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listings',
            name='bathrooms',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
