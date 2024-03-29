# Generated by Django 5.0.1 on 2024-01-07 11:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('AdminApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Creators',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FullName', models.CharField(max_length=50)),
                ('UsrName', models.CharField(max_length=50)),
                ('MusicRole', models.CharField(max_length=10)),
                ('Country', models.CharField(max_length=10)),
                ('Email', models.EmailField(max_length=50, unique=True)),
                ('Password', models.CharField(max_length=100)),
                ('Profile_Picture', models.ImageField(blank=True, null=True, upload_to='profile_pictures/')),
                ('Profile_Banner', models.ImageField(blank=True, null=True, upload_to='profile_banners/')),
                ('doj', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CollabNotifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Msg', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('Crid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Collab_notification_receiver', to='Creator.creators')),
                ('FlwCrid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Collab_notification_generator', to='Creator.creators')),
            ],
        ),
        migrations.CreateModel(
            name='Albums',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Album_Name', models.CharField(max_length=50)),
                ('Album_Cover', models.ImageField(blank=True, null=True, upload_to='Creator/Album_Covers')),
                ('CrId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Creator.creators')),
            ],
        ),
        migrations.CreateModel(
            name='CrPlaylist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PlaylistName', models.CharField(max_length=50)),
                ('Playlist_Cover', models.ImageField(blank=True, null=True, upload_to='Creator/CrPlaylist')),
                ('PlStatus', models.IntegerField(default=0)),
                ('CrId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Creator.creators')),
            ],
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_followed', models.DateTimeField(auto_now_add=True)),
                ('follower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following', to='Creator.creators')),
                ('following', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followers', to='Creator.creators')),
            ],
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('Crrole', models.CharField(max_length=50, null=True)),
                ('audio_file', models.FileField(upload_to='music/')),
                ('release_date', models.DateField()),
                ('cover_art', models.ImageField(upload_to='music_covers/')),
                ('c1role', models.CharField(blank=True, max_length=50, null=True)),
                ('c2role', models.CharField(blank=True, max_length=50, null=True)),
                ('c3role', models.CharField(blank=True, max_length=50, null=True)),
                ('Album', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Creator.albums')),
                ('CrId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Creator.creators')),
                ('Language', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='AdminApp.language')),
                ('Mood', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='AdminApp.musicmood')),
                ('collaborator_1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='collaborator_1', to='Creator.creators')),
                ('collaborator_2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='collaborator_2', to='Creator.creators')),
                ('collaborator_3', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='collaborator_3', to='Creator.creators')),
                ('genre', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='AdminApp.genre')),
            ],
        ),
        migrations.CreateModel(
            name='CrPlaylistItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CrPlid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Creator.crplaylist')),
                ('MusicId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Creator.music')),
            ],
        ),
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Msg', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('Crid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notification_receiver', to='Creator.creators')),
                ('FlwCrid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notification_generator', to='Creator.creators')),
            ],
        ),
    ]
