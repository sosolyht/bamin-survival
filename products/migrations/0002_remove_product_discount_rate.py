# Generated by Django 4.0.1 on 2022-02-05 21:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='discount_rate',
        ),
    ]