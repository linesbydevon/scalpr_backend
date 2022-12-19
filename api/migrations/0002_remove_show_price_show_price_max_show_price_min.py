# Generated by Django 4.1.4 on 2022-12-19 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='show',
            name='price',
        ),
        migrations.AddField(
            model_name='show',
            name='price_max',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AddField(
            model_name='show',
            name='price_min',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
    ]
