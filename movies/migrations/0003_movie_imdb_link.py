# Generated by Django 3.0.8 on 2021-01-23 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20191005_1614'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='imdb_link',
            field=models.URLField(blank=True, default='', null=True),
        ),
    ]
