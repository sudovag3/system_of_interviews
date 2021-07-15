# Generated by Django 2.2.10 on 2021-07-14 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название опроса')),
                ('date_of_start', models.DateTimeField(verbose_name='Дата начала опроса')),
                ('date_of_end', models.DateTimeField(verbose_name='Дата окончания опроса')),
                ('description', models.CharField(max_length=1000, verbose_name='Описание опроса')),
            ],
            options={
                'verbose_name': 'Опрос',
                'verbose_name_plural': 'Опросы',
            },
        ),
    ]
