# Generated by Django 4.0.1 on 2022-02-08 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('account', models.CharField(max_length=50)),
                ('nickname', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('phone', models.CharField(max_length=20, unique=True)),
                ('point', models.IntegerField()),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
