# Generated by Django 4.2.4 on 2023-08-25 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_album_year_of_release'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='year_of_release',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]