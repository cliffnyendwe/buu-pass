# Generated by Django 3.0 on 2022-02-18 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buupass', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='arrival_time',
        ),
        migrations.AddField(
            model_name='bus',
            name='booked_seat',
            field=models.ManyToManyField(blank=True, related_name='booked_seats', to='buupass.Seat'),
        ),
        migrations.AddField(
            model_name='seat',
            name='occupied',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='departure_time',
            field=models.DateField(),
        ),
    ]
