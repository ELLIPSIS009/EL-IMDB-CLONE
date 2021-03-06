# Generated by Django 2.2.6 on 2019-10-05 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('celebs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='Added Date')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(max_length=55, unique=True)),
                ('content', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='Added Date')),
                ('title', models.CharField(max_length=75)),
                ('release_year', models.CharField(max_length=4)),
                ('slug', models.SlugField(max_length=85)),
                ('imdb_rating', models.FloatField(blank=True, null=True, verbose_name='IMDB rating')),
                ('duration', models.SmallIntegerField(blank=True, default=0, help_text='in minutes', null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('trailer', models.URLField(blank=True, default='', help_text='trailer url (for now, ONLY youtube videos)', null=True)),
                ('source_content', models.URLField(blank=True, default='', null=True)),
                ('source_image', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MovieCrew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(blank=True, default='', help_text='e.g. short story, scrrenplay for writer, voice for cast', max_length=75)),
                ('screen_name', models.CharField(blank=True, default='', help_text="crew's name on movie", max_length=75)),
                ('crew', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_crews', to='celebs.Celebrity')),
                ('duty', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='celebs.Duty')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_crews', to='movies.Movie')),
            ],
        ),
    ]
