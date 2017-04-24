# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-31 05:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0039_pep_authors'),
    ]

    operations = [
        migrations.AddField(
            model_name='externalresource',
            name='submitter',
            field=models.ForeignKey(default=111, on_delete=django.db.models.deletion.CASCADE, related_name='externalresource_submitters', to=settings.AUTH_USER_MODEL, verbose_name='Добавил'),
        ),
        migrations.AddField(
            model_name='historicalplace',
            name='submitter',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='person',
            name='submitter',
            field=models.ForeignKey(default=111, on_delete=django.db.models.deletion.CASCADE, related_name='person_submitters', to=settings.AUTH_USER_MODEL, verbose_name='Добавил'),
        ),
        migrations.AddField(
            model_name='place',
            name='submitter',
            field=models.ForeignKey(default=111, on_delete=django.db.models.deletion.CASCADE, related_name='place_submitters', to=settings.AUTH_USER_MODEL, verbose_name='Добавил'),
        ),
        migrations.AddField(
            model_name='user',
            name='submitter',
            field=models.ForeignKey(default=111, on_delete=django.db.models.deletion.CASCADE, related_name='user_submitters', to=settings.AUTH_USER_MODEL, verbose_name='Добавил'),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='submitter',
            field=models.ForeignKey(default=111, on_delete=django.db.models.deletion.CASCADE, related_name='vacancy_submitters', to=settings.AUTH_USER_MODEL, verbose_name='Добавил'),
        ),
        migrations.AlterField(
            model_name='article',
            name='submitter',
            field=models.ForeignKey(default=111, on_delete=django.db.models.deletion.CASCADE, related_name='article_submitters', to=settings.AUTH_USER_MODEL, verbose_name='Добавил'),
        ),
        migrations.AlterField(
            model_name='book',
            name='submitter',
            field=models.ForeignKey(default=111, on_delete=django.db.models.deletion.CASCADE, related_name='book_submitters', to=settings.AUTH_USER_MODEL, verbose_name='Добавил'),
        ),
        migrations.AlterField(
            model_name='community',
            name='submitter',
            field=models.ForeignKey(default=111, on_delete=django.db.models.deletion.CASCADE, related_name='community_submitters', to=settings.AUTH_USER_MODEL, verbose_name='Добавил'),
        ),
        migrations.AlterField(
            model_name='discussion',
            name='submitter',
            field=models.ForeignKey(default=111, on_delete=django.db.models.deletion.CASCADE, related_name='discussion_submitters', to=settings.AUTH_USER_MODEL, verbose_name='Добавил'),
        ),
        migrations.AlterField(
            model_name='event',
            name='submitter',
            field=models.ForeignKey(default=111, on_delete=django.db.models.deletion.CASCADE, related_name='event_submitters', to=settings.AUTH_USER_MODEL, verbose_name='Добавил'),
        ),
        migrations.AlterField(
            model_name='pep',
            name='submitter',
            field=models.ForeignKey(default=111, on_delete=django.db.models.deletion.CASCADE, related_name='pep_submitters', to=settings.AUTH_USER_MODEL, verbose_name='Добавил'),
        ),
        migrations.AlterField(
            model_name='reference',
            name='submitter',
            field=models.ForeignKey(default=111, on_delete=django.db.models.deletion.CASCADE, related_name='reference_submitters', to=settings.AUTH_USER_MODEL, verbose_name='Добавил'),
        ),
        migrations.AlterField(
            model_name='version',
            name='submitter',
            field=models.ForeignKey(default=111, on_delete=django.db.models.deletion.CASCADE, related_name='version_submitters', to=settings.AUTH_USER_MODEL, verbose_name='Добавил'),
        ),
        migrations.AlterField(
            model_name='video',
            name='submitter',
            field=models.ForeignKey(default=111, on_delete=django.db.models.deletion.CASCADE, related_name='video_submitters', to=settings.AUTH_USER_MODEL, verbose_name='Добавил'),
        ),
    ]