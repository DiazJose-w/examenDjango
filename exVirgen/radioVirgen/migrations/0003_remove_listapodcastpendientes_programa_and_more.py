# Generated by Django 5.1.4 on 2025-02-18 17:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('radioVirgen', '0002_alter_listapodcastpendientes_programa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listapodcastpendientes',
            name='programa',
        ),
        migrations.AddField(
            model_name='listapodcastpendientes',
            name='podcast',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='podcastPendientes', to='radioVirgen.podcast'),
            preserve_default=False,
        ),
    ]
