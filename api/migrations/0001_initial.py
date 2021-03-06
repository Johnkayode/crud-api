# Generated by Django 4.0.3 on 2022-04-01 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=250, verbose_name='first name')),
                ('last_name', models.CharField(max_length=250, verbose_name='last name')),
                ('email', models.CharField(max_length=250, verbose_name='email')),
                ('city', models.CharField(max_length=20, verbose_name='city')),
                ('state', models.CharField(max_length=250, verbose_name='state')),
                ('phone_number', models.CharField(max_length=11, verbose_name='phone number')),
            ],
        ),
    ]
