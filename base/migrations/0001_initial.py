# Generated by Django 4.1.7 on 2023-07-03 19:53

import base.models
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BloodDonatedStudents',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=25)),
                ('blood_type', models.CharField(max_length=3)),
                ('roll_no', models.CharField(max_length=8, unique=True)),
                ('phone', models.CharField(max_length=10, unique=True)),
                ('donated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bloodreq',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('bloodGroup', models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('O+', 'O+'), ('O-', 'O-'), ('AB+', 'AB+'), ('AB-', 'AB-')], max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=25)),
                ('full_form', models.TextField(blank=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Explore',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('created_by', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to=base.models.Explore.get_image_path)),
            ],
        ),
        migrations.CreateModel(
            name='Fests',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, null=True)),
                ('full_form', models.TextField(blank=True)),
                ('description', models.TextField()),
                ('logo', models.ImageField(default='default_image.jpg', upload_to=base.models.Fests.get_image_path)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(default='default_image.jpg', upload_to=base.models.News.get_image_path)),
                ('created_by', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('time', models.TimeField(null=True)),
                ('date', models.DateField(null=True)),
                ('link', models.URLField(blank=True, null=True)),
                ('venue', models.CharField(max_length=200)),
                ('created_by', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Exploreimg',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to=base.models.Exploreimg.get_image_path)),
                ('explore', models.ForeignKey(blank=True, default=uuid.uuid4, on_delete=django.db.models.deletion.CASCADE, to='base.explore')),
            ],
        ),
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to=base.models.Carousel.get_image_path)),
                ('created_by', models.CharField(blank=True, max_length=200)),
                ('news', models.ForeignKey(blank=True, default=uuid.uuid4, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.news')),
                ('program', models.ForeignKey(blank=True, default=uuid.uuid4, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.program')),
            ],
        ),
        migrations.CreateModel(
            name='BloodDonation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=25)),
                ('roll_no', models.CharField(max_length=8, unique=True)),
                ('phone', models.CharField(max_length=10, unique=True)),
                ('blood_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.bloodreq')),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.course')),
            ],
        ),
    ]
