# Generated by Django 3.0.6 on 2020-07-04 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='charge',
            field=models.IntegerField(null=True),
        ),
    ]
