# Generated by Django 3.1.2 on 2020-10-10 20:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('circles', '0005_invitation'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ride',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified at')),
                ('avaliable_seats', models.PositiveSmallIntegerField(default=1)),
                ('comments', models.TextField(blank=True)),
                ('departure_location', models.CharField(max_length=255)),
                ('departure_date', models.DateTimeField()),
                ('arrival_location', models.CharField(max_length=255)),
                ('arrival_date', models.DateTimeField()),
                ('rating', models.FloatField(null=True)),
                ('is_active', models.BooleanField(default=False, help_text='Used for disabling the ride or marking it has finished', verbose_name='active status')),
                ('offeded_in', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='circles.circle')),
                ('offered_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('passengers', models.ManyToManyField(related_name='passengers', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Ride',
                'verbose_name_plural': 'Rides',
            },
        ),
    ]