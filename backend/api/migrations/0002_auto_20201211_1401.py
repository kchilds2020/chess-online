# Generated by Django 3.1.4 on 2020-12-11 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='losses',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='account',
            name='total_games',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='account',
            name='wins',
            field=models.IntegerField(default=0),
        ),
    ]
