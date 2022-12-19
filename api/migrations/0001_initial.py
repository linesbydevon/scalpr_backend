# Generated by Django 4.1.4 on 2022-12-19 00:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/images/')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=250, null=True)),
                ('phone_number', models.CharField(max_length=150)),
                ('website', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.CharField(default='no price information', max_length=100)),
                ('month', models.IntegerField()),
                ('day', models.IntegerField()),
                ('year', models.IntegerField()),
                ('door_time', models.CharField(max_length=100)),
                ('tickets_url', models.CharField(max_length=200, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/images/')),
                ('venue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shows', to='api.venue')),
            ],
        ),
    ]
