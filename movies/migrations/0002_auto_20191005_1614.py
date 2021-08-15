# Generated by Django 2.2.6 on 2019-10-05 16:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('celebs', '0002_auto_20191005_1614'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='added_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='movie',
            name='crews',
            field=models.ManyToManyField(related_name='movies', through='movies.MovieCrew', to='celebs.Celebrity'),
        ),
        migrations.AddField(
            model_name='movie',
            name='genres',
            field=models.ManyToManyField(related_name='movies', to='movies.Genre'),
        ),
        migrations.AlterUniqueTogether(
            name='movie',
            unique_together={('title', 'release_year')},
        ),
    ]
