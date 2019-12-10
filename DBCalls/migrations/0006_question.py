# Generated by Django 2.2.2 on 2019-06-10 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DBCalls', '0005_exhibit_module'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('queID', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('queTitle', models.CharField(max_length=100)),
                ('queType', models.CharField(max_length=100)),
                ('queExtras', models.TextField(blank=True)),
            ],
        ),
    ]