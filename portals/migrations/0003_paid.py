# Generated by Django 4.2.7 on 2023-11-29 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portals', '0002_alter_statement_ref'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('phone', models.CharField(max_length=50)),
                ('amount', models.IntegerField()),
            ],
        ),
    ]
