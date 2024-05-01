# Generated by Django 5.0.2 on 2024-04-25 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0005_activities_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='flights',
            name='image',
            field=models.ImageField(default='flight_images/default.jpg', upload_to='flight_images/'),
        ),
        migrations.AlterField(
            model_name='hotels',
            name='image',
            field=models.ImageField(upload_to='hotel_images/'),
        ),
    ]
