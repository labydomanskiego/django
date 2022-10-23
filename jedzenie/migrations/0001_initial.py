# Generated by Django 4.1.2 on 2022-10-23 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jedzenie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('danie', models.CharField(max_length=100)),
                ('kcal', models.IntegerField()),
                ('smaczne', models.BooleanField()),
                ('create_time', models.DateTimeField(verbose_name='create time')),
                ('last_edit_time', models.DateTimeField(verbose_name='last edit time')),
            ],
        ),
    ]
