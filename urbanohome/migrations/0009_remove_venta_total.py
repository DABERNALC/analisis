# Generated by Django 3.2.9 on 2021-11-11 21:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('urbanohome', '0008_auto_20211111_1548'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venta',
            name='total',
        ),
    ]
