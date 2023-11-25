# Generated by Django 4.2.7 on 2023-11-24 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam', models.CharField(max_length=50)),
                ('date', models.CharField(max_length=50)),
                ('time', models.CharField(max_length=50)),
                ('venue', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('county', models.CharField(default='Nairobi', max_length=50)),
                ('constituency', models.CharField(default='Embakasi', max_length=50)),
                ('ward', models.CharField(default='CBD', max_length=50)),
                ('location', models.CharField(max_length=50, null=True)),
                ('sub_location', models.CharField(max_length=50, null=True)),
                ('village', models.CharField(max_length=50, null=True)),
                ('town', models.CharField(default='Nakuru', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_number', models.IntegerField()),
                ('email', models.EmailField(max_length=50)),
                ('phone_number', models.IntegerField()),
                ('gender', models.CharField(max_length=50, null=True)),
                ('address', models.ManyToManyField(blank=True, to='portals.location')),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_name', models.CharField(max_length=50)),
                ('date', models.CharField(max_length=50)),
                ('time', models.CharField(max_length=50)),
                ('venue', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='John', max_length=50)),
                ('surname', models.CharField(default='Doe', max_length=50)),
                ('other_names', models.CharField(default='your_default_value', max_length=50)),
                ('regno', models.CharField(max_length=10, unique=True)),
                ('course', models.CharField(default=' Class B', max_length=15)),
                ('profile', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='portals.profile')),
            ],
        ),
    ]