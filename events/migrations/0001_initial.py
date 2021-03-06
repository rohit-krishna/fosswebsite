
from __future__ import unicode_literals

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
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('start_date', models.DateField(blank=True)),
                ('end_date', models.DateField(blank=True)),
                ('description', models.TextField(blank=True)),
                ('venue', models.CharField(blank=True, max_length=300)),
                ('trainer_bio', models.TextField(blank=True)),
                ('no_of_participants', models.IntegerField(blank=True, default=0)),
                ('level', models.CharField(choices=[('beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('expert', 'Expert')], max_length=100)),
                ('prerequisite', models.TextField(blank=True)),
                ('travel', models.TextField(blank=True)),
                ('accommodation', models.TextField(blank=True)),
                ('expense', models.FloatField(blank=True, default=0)),
                ('lab_requirements', models.TextField(blank=True)),
                ('icts_support', models.TextField(blank=True)),
                ('permissions', models.TextField(blank=True)),
                ('date_added', models.DateField(auto_now_add=True)),
                ('is_approved', models.BooleanField(default=False)),
                ('is_published', models.BooleanField(default=False)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EventImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='events/')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Event')),
            ],
        ),
    ]
