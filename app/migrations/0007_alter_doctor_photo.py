# Generated by Django 4.2.7 on 2024-01-05 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_doctor_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='static/img/doctor_profile_pic'),
        ),
    ]