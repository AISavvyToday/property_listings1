# Generated by Django 3.0.3 on 2020-02-19 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property_agency', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='phone',
            field=models.CharField(max_length=50),
        ),
    ]
