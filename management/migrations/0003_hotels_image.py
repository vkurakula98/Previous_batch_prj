# Generated by Django 5.0.2 on 2024-04-24 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_rename_activity_activities_rename_flight_flights_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotels',
            name='image',
            field=models.ImageField(default='path/to/default.jpg', upload_to='hotels'),
        ),
    ]