# Generated by Django 3.2.9 on 2021-11-14 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basketitem',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
