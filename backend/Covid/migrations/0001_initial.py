# Generated by Django 3.1.7 on 2021-02-28 11:36

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Covid_file',
            fields=[
                ('country', models.CharField(default='Unknown', max_length=20, primary_key=True, serialize=False)),
                ('confirmed_x', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=20), blank=True, null=True, size=None)),
                ('confirmed_y', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, null=True, size=None)),
                ('confirmed_total', models.IntegerField(blank=True, null=True)),
                ('deaths_x', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=20), blank=True, null=True, size=None)),
                ('deaths_y', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, null=True, size=None)),
                ('deaths_total', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
