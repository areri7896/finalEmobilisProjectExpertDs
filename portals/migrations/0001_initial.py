# Generated by Django 4.2.7 on 2023-11-23 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('county', models.CharField(max_length=50)),
                ('constituency', models.CharField(max_length=50)),
                ('ward', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('sub_location', models.CharField(max_length=50)),
                ('village', models.CharField(max_length=50)),
                ('town', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=50)),
                ('firstname', models.CharField(max_length=50)),
                ('other_names', models.CharField(max_length=50)),
                ('id_number', models.IntegerField()),
                ('email', models.EmailField(max_length=50)),
                ('phone_number', models.IntegerField()),
                ('gender', models.CharField(max_length=50)),
            ],
        ),
    ]
