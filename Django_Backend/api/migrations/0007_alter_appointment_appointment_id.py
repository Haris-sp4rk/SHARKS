# Generated by Django 3.2.9 on 2021-12-20 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_appointment_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='appointment_id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
