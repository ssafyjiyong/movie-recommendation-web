from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('profile_path', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('profile_path', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_id', models.IntegerField(null=True)),
                ('title', models.CharField(max_length=100)),
                ('original_language', models.CharField(max_length=20, null=True)),
                ('overview', models.TextField(null=True)),
                ('release_date', models.TextField(null=True)),
                ('runtime', models.IntegerField(null=True)),
                ('poster_path', models.TextField(null=True)),
                ('popularity', models.FloatField(null=True)),
                ('tagline', models.TextField(null=True)),
                ('vote_average', models.FloatField(null=True)),
                ('vote_count', models.IntegerField(null=True)),
                ('video', models.TextField(null=True)),
                ('actors', models.ManyToManyField(related_name='movies', to='movies.actor')),
                ('director', models.ManyToManyField(related_name='movies', to='movies.director')),
                ('genres', models.ManyToManyField(related_name='movies', to='movies.genre')),
                ('hate_users', models.ManyToManyField(related_name='hate_movies', to=settings.AUTH_USER_MODEL)),
                ('like_users', models.ManyToManyField(related_name='like_movies', to=settings.AUTH_USER_MODEL)),
                ('normal_users', models.ManyToManyField(related_name='normal_movies', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.TextField(null=True)),
                ('url', models.TextField(null=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie')),
            ],
        ),
    ]
