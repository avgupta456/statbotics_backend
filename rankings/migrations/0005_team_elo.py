# Generated by Django 3.0.6 on 2020-05-19 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rankings', '0004_auto_20200519_1415'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='elo',
            field=models.DecimalField(decimal_places=2, default=-1, max_digits=6),
            preserve_default=False,
        ),
    ]