# Generated by Django 3.2.7 on 2021-10-26 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.TextField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='order',
            name='OrderDate',
            field=models.DateTimeField(),
        ),
    ]