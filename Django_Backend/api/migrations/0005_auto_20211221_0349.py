# Generated by Django 3.2.9 on 2021-12-20 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20211219_1659'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='timing',
        ),
        migrations.AddField(
            model_name='appointment',
            name='end_timing',
            field=models.TextField(default='6:00'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='start_timing',
            field=models.TextField(default='9:00'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='status',
            field=models.TextField(choices=[('rejected', 'REJECTED'), ('completed', 'COMPLETED'), ('pending', 'PENDING'), ('on going', 'ON GOING'), ('on hold', 'ON HOLD')], default='pending'),
        ),
    ]