# Generated by Django 5.1.1 on 2024-09-07 18:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=200, verbose_name='место')),
                ('time', models.DateTimeField(verbose_name='время')),
                ('action', models.CharField(max_length=400, verbose_name='действие')),
                ('is_enjoyable', models.BooleanField(default=False, verbose_name='признак приятности')),
                ('periodicity', models.IntegerField(default=1, verbose_name='периодичность')),
                ('reward', models.CharField(blank=True, max_length=400, null=True, verbose_name='вознаграждение')),
                ('time_to_complete', models.IntegerField(verbose_name='время на выполнение')),
                ('is_public', models.BooleanField(default=False, verbose_name='признак публичности')),
                ('related_habit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='habits.habit', verbose_name='связанная привычка')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'привычка',
                'verbose_name_plural': 'привычки',
            },
        ),
    ]
