# Generated by Django 4.2.7 on 2023-11-30 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portals', '0003_paid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paid',
            name='amount',
            field=models.CharField(max_length=50),
        ),
    ]
